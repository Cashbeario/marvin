import asyncio
import json
from agents.base_agent import BaseAgent
from core.workspace import CognitiveWorkspace, WorkspaceItem
from core.models import MessageEnvelope

class OrchestratorAgent(BaseAgent):
    def __init__(self):
        super().__init__(agent_id="orchestrator_agent_001", role="Orchestrator", agent_type="executive")
        self.workspace = CognitiveWorkspace()

    async def connect(self):
        await super().connect()

        # Subscribe to new workspace items
        await self.nc.subscribe("marvin.workspace.item.new.v1", cb=self.handle_new_item)

        # Subscribe to external events
        await self.nc.subscribe("marvin.events.input.received.v1", cb=self.handle_external_input)

        # Start the ignition cycle
        asyncio.create_task(self.ignition_loop())
        print("Orchestrator ignition loop started.")

    async def handle_external_input(self, msg):
        print(f"Orchestrator received external input: {msg.data.decode()}")
        self.workspace.phase = "planning"
        # In a real scenario, this would trigger the Planner Agent

    async def handle_new_item(self, msg):
        try:
            envelope = MessageEnvelope.model_validate_json(msg.data)
            content = envelope.content

            item = WorkspaceItem(
                sender_agent_id=envelope.sender["agent_id"],
                sender_agent_type="unknown", # Should be in sender metadata
                content_type=content["content_type"],
                content=content["content"],
                urgency=content.get("urgency", 0.0),
                confidence=content.get("confidence", 1.0)
            )
            self.workspace.add_item(item)
        except Exception as e:
            print(f"Error adding workspace item: {e}")

    async def ignition_loop(self):
        while self.status != "shutdown":
            winner = self.workspace.ignite()
            if winner:
                print(f"IGNITION: Winner {winner.item_id} from {winner.sender_agent_id}")
                # Global Broadcast
                await self.nc.publish("marvin.workspace.broadcast.v1", winner.model_dump_json().encode())
                winner.status = "broadcast"

                # Update phase based on item content if necessary
                if winner.content_type == "plan":
                    self.workspace.phase = "executing"

            await asyncio.sleep(0.5) # Fast lane interval (SDD: 500ms)

async def main():
    orch = OrchestratorAgent()
    await orch.connect()
    while True:
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())
