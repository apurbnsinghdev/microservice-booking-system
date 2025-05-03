from functools import lru_cache
from fastapi import FastAPI
from .routes import cart
from .database import init_cart_db, settings

app = FastAPI(title="Cart Service")

# Settings
@lru_cache
def get_settings():
    return settings

# Run DB initialization on startup
@app.on_event("startup")
def on_startup():
    init_cart_db()

app.include_router(cart.router)