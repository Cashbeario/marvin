import asyncio
import json
import nats

async def test_sor():
    nc = await nats.connect("nats://localhost:4222")
    test_event = {
        "conversation_id": "test_conv_1",
        "sender": {"agent_id": "test_agent", "tribe_id": None, "domain": "domain_1"},
        "content": {"message": "Hello MARVIN SOR"},
        "plan_id": "test_plan_1"
    }
    response = await nc.request("marvin.sor.append.task_start.v1", json.dumps(test_event).encode(), timeout=2)
    print(f"SOR response: {response.data.decode()}")
    js = nc.jetstream()
    sub = await js.pull_subscribe("marvin.sor.append.v1", "test_consumer")
    msgs = await sub.fetch(1)
    for msg in msgs:
        print(f"Fetched from SOR stream: {msg.data.decode()}")
        await msg.ack()
    await nc.close()

if __name__ == "__main__":
    asyncio.run(test_sor())
