from fastapi import FastAPI
from core.config import settings
from core.routers import health
from core.events import on_startup, on_shutdown
from core.logging_config import setup_logging

# Configurar logging
setup_logging()

app = FastAPI(title=settings.PROJECT_NAME)

@app.on_event("startup")
async def startup_event():
    await on_startup(app)

@app.on_event("shutdown")
async def shutdown_event():
    await on_shutdown(app)

app.include_router(health.router, prefix=settings.API_VERSION)
