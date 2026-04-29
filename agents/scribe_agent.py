import asyncio
import json
import hashlib
from nats.aio.client import Client as NATS
from cryptography.hazmat.primitives.asymmetric import ed25519
from core.models import SOREntry, MessageEnvelope

class ScribeAgent:
    def __init__(self, domain_id: str):
        self.domain_id = domain_id
        self.agent_id = "scribe_agent_001"
        self.private_key = ed25519.Ed25519PrivateKey.generate()
        self.public_key = self.private_key.public_key()
        self.previous_hash = "0" * 64
        self.sequence = 0
        self.nc = NATS()

    async def connect(self):
        await self.nc.connect("nats://localhost:4222")
        self.js = self.nc.jetstream()
        await self.nc.subscribe("marvin.sor.append.>", cb=self.handle_sor_request)
        print("ScribeAgent connected.")

    async def handle_sor_request(self, msg):
        try:
            data = json.loads(msg.data.decode())
            event_type = msg.subject.split('.')[-2]
            entry = await self.create_entry(
                event_type=event_type,
                agent_id=data.get("sender", {}).get("agent_id", "unknown"),
                conversation_id=data.get("conversation_id", "none"),
                payload=data.get("content", {}),
                plan_id=data.get("plan_id")
            )
            await self.js.publish("marvin.sor.append.v1", entry.model_dump_json().encode())
            if msg.reply:
                await self.nc.publish(msg.reply, b"OK")
        except Exception as e:
            print(f"Error: {e}")

    async def create_entry(self, event_type, agent_id, conversation_id, payload, plan_id=None) -> SOREntry:
        self.sequence += 1
        content_to_hash = {"sequence": self.sequence, "event_type": event_type, "agent_id": agent_id, "payload": payload, "previous_hash": self.previous_hash}
        content_str = json.dumps(content_to_hash, sort_keys=True)
        current_hash = hashlib.sha256(content_str.encode()).hexdigest()
        signature = self.private_key.sign(current_hash.encode()).hex()
        entry = SOREntry(sequence=self.sequence, event_type=event_type, agent_id=agent_id, conversation_id=conversation_id, plan_id=plan_id, payload=payload, previous_hash=self.previous_hash, hash=current_hash, signature=signature)
        self.previous_hash = current_hash
        return entry

async def main():
    scribe = ScribeAgent(domain_id="domain_1")
    await scribe.connect()
    while True: await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())
