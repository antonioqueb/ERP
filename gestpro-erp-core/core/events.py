import logging
from fastapi import FastAPI

# Crear el logger usando el módulo de logging
logger = logging.getLogger("gestpro-erp-core")

async def on_startup(app: FastAPI):
    logger.info("Gestpro-ERP Core iniciado.")

async def on_shutdown(app: FastAPI):
    logger.info("Gestpro-ERP Core apagado.")
