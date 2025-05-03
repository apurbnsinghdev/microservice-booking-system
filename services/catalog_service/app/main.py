from functools import lru_cache
from fastapi import FastAPI
from .config import Settings
from .database import init_catalog_db, settings
from .routes import categories, subcategories, services

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))


app = FastAPI(title="Catalog Service")

# Settings
@lru_cache
def get_settings():
    return settings

# Run DB initialization on startup
@app.on_event("startup")
def on_startup():
    init_catalog_db()

app.include_router(categories.router)
app.include_router(subcategories.router)
app.include_router(services.router)

