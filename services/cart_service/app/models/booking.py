from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime


class Booking(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int
    service_id: int
    partner_id: int
    slot_time: datetime
    status: str = Field(default="pending")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
