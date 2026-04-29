import asyncio
import json
import nats
from agents.base_agent import BaseAgent

async def test_base_agent():
    nc = await nats.connect("nats://localhost:4222")
    sub_reg = await nc.subscribe("marvin.agents.register.v1")
    sub_ws = await nc.subscribe("marvin.workspace.item.new.v1")

    agent = BaseAgent(agent_id="test_cognitive_001", role="Reasoner", agent_type="cognitive")
    await agent.connect()
    await agent.publish_to_workspace({"analysis": "Thinking..."}, "observation")

    msg_reg = await sub_reg.next_msg(timeout=2)
    print(f"Registration: {msg_reg.data.decode()}")
    msg_ws = await sub_ws.next_msg(timeout=2)
    print(f"Workspace: {msg_ws.data.decode()}")

    await agent.shutdown()
    await nc.close()

if __name__ == "__main__":
    asyncio.run(test_base_agent())
