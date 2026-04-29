import asyncio
import json
from typing import Dict, Any, Callable

class MCPHost:
    def __init__(self):
        self._tool_map: Dict[str, Callable] = {}

    def register_tool(self, name: str, func: Callable):
        self._tool_map[name] = func
        print(f"Tool {name} registered.")

    async def call_tool(self, name: str, args: Dict[str, Any]) -> Any:
        if name not in self._tool_map:
            raise ValueError(f"Tool {name} not found.")

        print(f"Calling tool {name} with args {args}")
        if asyncio.iscoroutinefunction(self._tool_map[name]):
            return await self._tool_map[name](**args)
        else:
            return self._tool_map[name](**args)

# Mock Tool Functions
async def mock_write_file(filepath: str, content: str):
    return {"status": "success", "filepath": filepath}

async def mock_read_file(filepath: str):
    return {"status": "success", "content": "Mock content for " + filepath}

async def main():
    host = MCPHost()
    host.register_tool("write_file", mock_write_file)
    host.register_tool("read_file", mock_read_file)

    res1 = await host.call_tool("write_file", {"filepath": "test.txt", "content": "hello"})
    print(f"Result 1: {res1}")

    res2 = await host.call_tool("read_file", {"filepath": "test.txt"})
    print(f"Result 2: {res2}")

if __name__ == "__main__":
    asyncio.run(main())
