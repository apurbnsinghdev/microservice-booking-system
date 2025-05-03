from pydantic import BaseModel

class HealthResponse(BaseModel):
    status: str
    service: str
    message: str

class SlotResponse(BaseModel):
    status:str
    slot: str
    service_id:int
    partner_id:int

class MessageResponse(BaseModel):
    message: str

class ErrorResponse(BaseModel):
    error: str