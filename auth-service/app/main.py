from fastapi import FastAPI
from app.config import settings
from app.events import on_startup, on_shutdown
from app.logging_config import setup_logging
from app.routers import auth  # Importa el router de autenticación

# Configurar logging
setup_logging()

app = FastAPI(title=settings.PROJECT_NAME)

@app.get("/health")
async def health_check():
    return {"status": "auth-service is healthy"}

@app.on_event("startup")
async def startup_event():
    await on_startup(app)

@app.on_event("shutdown")
async def shutdown_event():
    await on_shutdown(app)

# Registrar rutas
app.include_router(auth.router, prefix=settings.API_VERSION)
