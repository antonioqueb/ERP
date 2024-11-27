# db-service/app/events.py

import logging
from fastapi import FastAPI

logger = logging.getLogger("gestpro-erp-db-service")

async def on_startup(app: FastAPI):
    logger.info("Gestpro-ERP Database Service iniciado.")

async def on_shutdown(app: FastAPI):
    logger.info("Gestpro-ERP Database Service apagado.")
