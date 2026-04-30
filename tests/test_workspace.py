import asyncio
import json
import nats
from agents.base_agent import BaseAgent
from agents.orchestrator_agent import OrchestratorAgent

async def test_workspace_ignition():
    # Start Orchestrator
    orch = OrchestratorAgent()
    await orch.connect()

    # Start a test agent
    agent = BaseAgent(agent_id="test_agent_1", role="Reasoner", agent_type="cognitive")
    await agent.connect()

    # Subscribe to broadcast
    nc = await nats.connect("nats://localhost:4222")
    sub_broadcast = await nc.subscribe("marvin.workspace.broadcast.v1")

    # Agent posts item
    await agent.publish_to_workspace({"fact": "NATS is fast"}, "observation", urgency=0.8)

    # Wait for broadcast
    msg = await sub_broadcast.next_msg(timeout=5)
    data = json.loads(msg.data.decode())
    print(f"Broadcast received: {data['content']}")

    assert data['sender_agent_id'] == "test_agent_1"
    assert data['content']['fact'] == "NATS is fast"

    await agent.shutdown()
    await orch.shutdown()
    await nc.close()

if __name__ == "__main__":
    asyncio.run(test_workspace_ignition())
