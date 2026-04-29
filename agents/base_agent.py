import asyncio
import json
import uuid
from datetime import datetime
from typing import Optional, List, Any
import nats
from nats.aio.client import Client as NATS
from core.models import MessageEnvelope

class BaseAgent:
    def __init__(self, agent_id: str, role: str, agent_type: str, tribe_id: Optional[str] = None):
        self.agent_id = agent_id
        self.role = role
        self.agent_type = agent_type
        self.tribe_id = tribe_id
        self.domain = "domain_1"
        self.nc = NATS()
        self.js = None
        self.status = "standby"
        self.reliability_score = 1.0

    async def connect(self):
        await self.nc.connect("nats://localhost:4222")
        self.js = self.nc.jetstream()
        self.status = "active"
        await self.register_capabilities()
        asyncio.create_task(self.heartbeat())
        print(f"Agent {self.agent_id} connected.")

    async def register_capabilities(self):
        registration = {"agent_id": self.agent_id, "agent_role": self.role, "agent_type": self.agent_type, "tribe_id": self.tribe_id, "status": self.status, "reliability_score": self.reliability_score, "timestamp": datetime.utcnow().isoformat()}
        await self.nc.publish("marvin.agents.register.v1", json.dumps(registration).encode())

    async def heartbeat(self):
        while self.status != "shutdown":
            heartbeat_data = {"agent_id": self.agent_id, "timestamp": datetime.utcnow().isoformat(), "status": self.status}
            await self.nc.publish(f"marvin.health.{self.agent_id}.heartbeat", json.dumps(heartbeat_data).encode())
            await asyncio.sleep(5)

    async def publish_to_workspace(self, content: Any, content_type: str, urgency: float = 0.0, confidence: float = 1.0):
        envelope = MessageEnvelope(conversation_id="global", sender={"agent_id": self.agent_id, "tribe_id": self.tribe_id, "domain": self.domain}, receiver="workspace", performative="inform", content={"content_type": content_type, "content": content, "urgency": urgency, "confidence": confidence})
        await self.nc.publish("marvin.workspace.item.new.v1", envelope.model_dump_json().encode())

    async def shutdown(self):
        self.status = "shutdown"
        await self.nc.close()
