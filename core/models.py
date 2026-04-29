from pydantic import BaseModel, Field
from typing import Any, Optional
from datetime import datetime
import uuid

class MessageEnvelope(BaseModel):
    message_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    conversation_id: str
    plan_id: Optional[str] = None
    sender: dict
    receiver: str
    timestamp: str = Field(default_factory=lambda: datetime.utcnow().isoformat())
    sequence: int = 0
    performative: str
    content: Any
    schema_version: str = "1.0"
    sor_required: bool = True

class SOREntry(BaseModel):
    sor_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    sequence: int
    timestamp: str = Field(default_factory=lambda: datetime.utcnow().isoformat())
    event_type: str
    agent_id: str
    plan_id: Optional[str] = None
    conversation_id: str
    payload: Any
    previous_hash: str
    hash: str
    signature: str
