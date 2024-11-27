# gestpro-erp-core/main.py

from fastapi import FastAPI, Depends, HTTPException
from core.config import settings
from core.logging_config import setup_logging
from core.routers import health
from core.events import on_startup, on_shutdown
from core.middleware.auth import check_token

# Configurar logging global
setup_logging(settings)

# Crear instancia de FastAPI
app = FastAPI(title=settings.PROJECT_NAME)

@app.on_event("startup")
async def startup_event():
    await on_startup(app)

@app.on_event("shutdown")
async def shutdown_event():
    await on_shutdown(app)

# Registrar rutas
app.include_router(health.router, prefix=settings.API_VERSION)

# Aplica el middleware para las rutas protegidas
@app.get("/api/v1/protected-route")
async def protected_route(user=Depends(check_token)):
    # Si el token es válido, la solicitud continúa aquí
    return {"message": "This is a protected route", "user": user}

