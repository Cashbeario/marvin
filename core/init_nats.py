import asyncio
import nats
from nats.js.api import StreamConfig, RetentionPolicy, StorageType

async def init_nats():
    nc = await nats.connect("nats://localhost:4222")
    js = nc.jetstream()

    streams = [
        {"name": "MARVIN_EVENTS", "subjects": ["marvin.events.>"]},
        {"name": "MARVIN_WORKSPACE", "subjects": ["marvin.workspace.>"]},
        {"name": "MARVIN_PLANS", "subjects": ["marvin.plans.>"]},
        {"name": "MARVIN_TOOLCALLS", "subjects": ["marvin.toolcalls.>"]},
        {"name": "MARVIN_SOR", "subjects": ["marvin.sor.>"]},
        {"name": "MARVIN_SELFIMPROVE", "subjects": ["marvin.selfimprove.>"]},
        {"name": "MARVIN_COUNCIL", "subjects": ["marvin.council.>"]},
        {"name": "MARVIN_BACKUP", "subjects": ["marvin.backup.>"]},
        {"name": "MARVIN_REPLAY", "subjects": ["marvin.replay.>"]},
        {"name": "MARVIN_ARA", "subjects": ["marvin.ara.>"]},
    ]

    for stream in streams:
        try:
            await js.add_stream(name=stream["name"], subjects=stream["subjects"], config=StreamConfig(
                retention=RetentionPolicy.LIMITS,
                storage=StorageType.FILE,
                num_replicas=1,
                max_age=7 * 24 * 3600,
                max_msg_size=8 * 1024 * 1024,
            ))
            print(f"Stream {stream['name']} created.")
        except Exception as e:
            print(f"Error creating stream {stream['name']}: {e}")

    await nc.close()

if __name__ == "__main__":
    asyncio.run(init_nats())
