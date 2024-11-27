# gestpro-erp-core/main.py
from fastapi import FastAPI, Depends
from core.config import settings
from core.logging_config import setup_logging
from core.routers import health
from core.events import on_startup, on_shutdown
from core.middleware.auth import check_token  # Importa el middleware de autenticación

# Configurar logging global
setup_logging(settings)

# Crear instancia de FastAPI
app = FastAPI(title=settings.PROJECT_NAME)

# Registrar settings en el estado de la aplicación
app.state.settings = settings

@app.on_event("startup")
async def startup_event():
    await on_startup(app)

@app.on_event("shutdown")
async def shutdown_event():
    await on_shutdown(app)

# Registrar rutas
app.include_router(health.router, prefix=settings.API_VERSION)

# Ruta protegida que usa el middleware para validar tokens
@app.get("/api/v1/protected-route")
async def protected_route(user=Depends(check_token)):
    """
    Ruta protegida que requiere un token válido para el acceso.

    Args:
        user (dict): Información del usuario autenticado obtenida del token.

    Returns:
        dict: Mensaje de acceso permitido con los datos del usuario.
    """
    return {"message": "This is a protected route", "user": user}
