import asyncio
import json
import redis.asyncio as redis
from typing import Optional, Any

class MemoryManager:
    def __init__(self, redis_url: str = "redis://localhost:6379"):
        self.redis_url = redis_url
        self.r = None

    async def connect(self):
        self.r = redis.from_url(self.redis_url)
        print("MemoryManager (L0) connected to Redis.")

    # L0: Working Memory (Redis)
    async def set_working(self, key: str, value: Any, ttl: int = 3600):
        await self.r.set(f"marvin:l0:{key}", json.dumps(value), ex=ttl)

    async def get_working(self, key: str) -> Optional[Any]:
        data = await self.r.get(f"marvin:l0:{key}")
        return json.loads(data) if data else None

    # L1: Episodic Memory (Mock Vector DB for now)
    async def store_episode(self, agent_id: str, content: Any):
        # In Phase 1, we mock this by just logging. Implementation with Qdrant/pgvector in Phase 4.
        print(f"STORE_EPISODE: Agent {agent_id} -> {content}")

    # L2: Semantic Memory (Mock Knowledge Graph for now)
    async def store_fact(self, subject: str, relation: str, object: str):
        # Implementation with Neo4j in Phase 4.
        print(f"STORE_FACT: {subject} --({relation})--> {object}")

async def main():
    mem = MemoryManager()
    await mem.connect()
    await mem.set_working("test_key", {"data": 123})
    val = await mem.get_working("test_key")
    print(f"L0 Get Result: {val}")

if __name__ == "__main__":
    asyncio.run(main())
