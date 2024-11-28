# db-service/app/main.py

from fastapi import FastAPI
from app.config import settings
from app.routers import health
from app.events import on_startup, on_shutdown
from app.logging_config import setup_logging

# Configurar logging
setup_logging()

# Crear la instancia de la aplicación FastAPI
app = FastAPI(title=settings.project_name)

@app.on_event("startup")
async def startup_event():
    """Evento de inicio de la aplicación."""
    await on_startup(app)

@app.on_event("shutdown")
async def shutdown_event():
    """Evento de cierre de la aplicación."""
    await on_shutdown(app)

# Registrar el router de salud
app.include_router(health.router, prefix=settings.api_version)
