from fastapi import FastAPI
from .routes import slot_routes

app = FastAPI()

app.include_router(slot_routes.router, prefix="/slot", tags=["Slot"])