# services/slot_service/app/routes.py
from fastapi import APIRouter, Depends, HTTPException
from app.redis_client import set_slot, get_slot, delete_slot
from app.models import HealthResponse, SlotResponse, MessageResponse, ErrorResponse

router = APIRouter()

def skip_auth():
    return

@router.get("/health", response_model=HealthResponse)
@router.get("/ping", response_model=HealthResponse)
@router.get("/", response_model=HealthResponse)
async def health_check():
    return {"status": "ok", "service": "slot_service", "message": "pong"}

@router.post("/{service_id}/{partner_id}/{slot_time}/available")
async def set_slot_available(service_id:int, partner_id: int, slot_time: str):
    slot_key = f"slot:{partner_id}:{slot_time}:{slot_time}"
    current = await get_slot(slot_key)
    if current == "booked":
        raise HTTPException(status_code=400, detail="Slot not available. Already Booked")
    slot_value = "available"
    await set_slot(slot_key, slot_value) 
    return {"status": "available", "slot": slot_time, "service_id": service_id, "partner_id": partner_id}

@router.post("/{service_id}/{partner_id}/{slot_time}/book", dependencies=[Depends(skip_auth)], response_model=MessageResponse)
async def book_slot(service_id:int, partner_id: int, slot_time: str):
    slot_kye = f"slot:{service_id}:{partner_id}:{slot_time}"
    current = await get_slot(slot_kye)
    if current == "available":
        slot_value = "booked"
        await set_slot(slot_kye, slot_value) 
        return {"status": "booked", "slot": slot_time, "service_id": service_id, "partner_id": partner_id}
    else:
        raise HTTPException(status_code=400, detail="Slot is not available")
    
    
@router.get("/{service_id}/{partner_id}/{slot_time}", dependencies=[Depends(skip_auth)], response_model=SlotResponse | ErrorResponse)
async def check_slot(service_id:int, partner_id: int, slot_time: str):
    slot_kye = f"slot:{service_id}:{partner_id}:{slot_time}"
    status  = await get_slot(slot_kye)
    if not status:
        raise HTTPException(status_code=404, detail="Slot not found")
    return {"status": status, "slot": slot_time, "service_id": service_id, "partner_id": partner_id}

@router.delete("/{service_id}/{partner_id}/:{slot_time}", response_model=MessageResponse)
async def remove_slot(service_id:int, partner_id: int, slot_time : str):
    slot_kye = f"slot:{service_id}:{partner_id}:{slot_time}"
    await delete_slot(slot_kye)
    return {"message": "Slot removed"}