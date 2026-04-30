import asyncio
import json
import time
from typing import List, Dict, Optional, Any
from pydantic import BaseModel, Field
import uuid

class WorkspaceItem(BaseModel):
    item_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    sender_agent_id: str
    sender_agent_type: str
    timestamp: float = Field(default_factory=time.time)
    content_type: str
    content: Any
    urgency: float = 0.0
    confidence: float = 0.0
    salience_score: float = 0.0
    status: str = "pending" # pending | ignited | inhibited | broadcast | archived

class CognitiveWorkspace:
    def __init__(self):
        self.workspace_id = str(uuid.uuid4())
        self.items: Dict[str, WorkspaceItem] = {}
        self.phase = "idle" # idle | planning | executing | validating | broadcasting | done
        self.tau = 0.5 # Adaptive threshold

    def add_item(self, item: WorkspaceItem):
        self.items[item.item_id] = item
        print(f"Item {item.item_id} added to workspace.")

    def compute_salience(self, item: WorkspaceItem, goal_similarity: float = 0.0) -> float:
        # weights from SDD
        w_urgency = 0.40
        w_goal_sim = 0.25
        w_recency = 0.15
        w_confidence = 0.20

        # Simplified recency: 1.0 if brand new, decaying to 0 over 60 seconds
        recency = max(0, 1.0 - (time.time() - item.timestamp) / 60.0)

        score = (w_urgency * item.urgency +
                 w_goal_sim * goal_similarity +
                 w_recency * recency +
                 w_confidence * item.confidence)

        # Temperature sharpening (SDD: T=0.7)
        T = 0.7
        item.salience_score = score ** (1/T)
        return item.salience_score

    def ignite(self) -> Optional[WorkspaceItem]:
        # Filter pending items
        candidates = [item for item in self.items.values() if item.status == "pending"]
        if not candidates:
            return None

        # Update salience for all candidates
        for item in candidates:
            self.compute_salience(item)

        # Winner-take-all
        winner = max(candidates, key=lambda x: x.salience_score)

        if winner.salience_score >= self.tau:
            winner.status = "ignited"
            # Inhibit others
            for item in candidates:
                if item.item_id != winner.item_id:
                    item.status = "inhibited"
            return winner

        return None
