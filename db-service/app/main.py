# db-service/app/main.py

from fastapi import FastAPI
from app.config import settings
from app.routers import health
from app.events import on_startup, on_shutdown
from app.logging_config import setup_logging

# Configurar logging
setup_logging()

app = FastAPI(title=settings.project_name)


@app.on_event("startup")
async def startup_event():
    await on_startup(app)

@app.on_event("shutdown")
async def shutdown_event():
    await on_shutdown(app)

app.include_router(health.router, prefix=settings.API_VERSION)
