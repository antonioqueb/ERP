from fastapi import FastAPI
from core.config import settings
from core.logging_config import setup_logging
from core.routers import health
from core.events import on_startup, on_shutdown

# Configurar logging global
setup_logging(settings)

# Crear instancia de FastAPI
app = FastAPI(title=settings.PROJECT_NAME)

# Registrar settings en el estado de la aplicación (opcional)
app.state.settings = settings

@app.on_event("startup")
async def startup_event():
    await on_startup(app)

@app.on_event("shutdown")
async def shutdown_event():
    await on_shutdown(app)

# Registrar routers
app.include_router(health.router, prefix=settings.API_VERSION)
