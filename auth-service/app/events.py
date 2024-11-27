import logging
from fastapi import FastAPI

logger = logging.getLogger("auth-service")

async def on_startup(app: FastAPI):
    logger.info("Auth Service iniciado.")

async def on_shutdown(app: FastAPI):
    logger.info("Auth Service apagado.")
