from typing import List
from pydantic import BaseModel
from datetime import datetime

class CartItemResponse(BaseModel):
    id: int
    service_id: int
    partner_id: int
    quantity: int

    class Config:
        orm_mode = True

class CartResponse(BaseModel):
    id: int
    user_id: int
    service_id: int
    items: List[CartItemResponse]

    class Config:
        orm_mode = True


class BookingResponse(BaseModel):
    id: int
    user_id: int
    service_id: int
    partner_id: int
    slot_time: datetime
    status: str
    created_at: datetime

    class Config:
        from_attributes = True

dummy_cart_response = {
    "id": 1,
    "user_id": 1,
    "items": [
        {
            "id": 101,
            "cart_id": 1,
            "service_id": 10,
            "partner_id": 5,
            "slot_time": "2025-05-03T10:00:00",
            "quantity": 2
        },
        {
            "id": 102,
            "cart_id": 1,
            "service_id": 12,
            "partner_id": 7,
            "slot_time": "2025-05-03T15:00:00",
            "quantity": 2
        }
    ]
}
