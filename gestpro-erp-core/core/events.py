import logging
from fastapi import FastAPI
from httpx import AsyncClient

logger = logging.getLogger("gestpro-erp-core")

async def on_startup(app: FastAPI):
    logger.info("Iniciando Gestpro-ERP Core...")
    # Verificar conexión a db-service (opcional)
    async with AsyncClient() as client:
        try:
            response = await client.get(f"{app.state.settings.DATABASE_SERVICE_URL}/health")
            if response.status_code == 200:
                logger.info("db-service está disponible.")
            else:
                logger.warning("db-service no responde correctamente.")
        except Exception as e:
            logger.error(f"No se pudo conectar a db-service: {e}")
            raise RuntimeError("El servicio db-service no está disponible.")

async def on_shutdown(app: FastAPI):
    logger.info("Apagando Gestpro-ERP Core...")
