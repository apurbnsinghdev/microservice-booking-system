from typing import List, Optional
from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime

class CartItem(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    cart_id: int = Field(foreign_key="cart.id")
    service_id: int
    partner_id: int
    quantity: int = 1

class Cart(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(index=True, unique=True)
    items: List["CartItem"] = Relationship(back_populates="cart")

    CartItem.cart = Relationship(back_populates="items")

cart_items = [
    {
        "service_id": 10,
        "partner_id": 5,
        "slot_time": datetime.fromisoformat("2025-05-03T10:00:00")
    },
    {
        "service_id": 12,
        "partner_id": 7,
        "slot_time": datetime.fromisoformat("2025-05-03T15:00:00")
    }
]
