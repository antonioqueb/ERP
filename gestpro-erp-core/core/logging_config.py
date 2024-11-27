import logging
from logging.config import dictConfig
from core.config import settings

# Configuración de logging dinámica basada en el entorno
def get_logging_config():
    return {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            },
            "detailed": {
                "format": (
                    "%(asctime)s - %(name)s - %(levelname)s - "
                    "[%(filename)s:%(lineno)d] - %(message)s"
                ),
            },
        },
        "handlers": {
            "console": {
                "level": settings.LOG_LEVEL,  # Nivel desde settings
                "formatter": "detailed" if settings.DEBUG else "default",
                "class": "logging.StreamHandler",
            },
            "file": {
                "level": settings.LOG_LEVEL,  # Nivel desde settings
                "formatter": "detailed",
                "class": "logging.FileHandler",
                "filename": settings.LOG_FILE,  # Archivo de log desde settings
            },
        },
        "loggers": {
            "gestpro-erp-core": {  # Logger principal de la aplicación
                "handlers": ["console", "file"],
                "level": settings.LOG_LEVEL,
                "propagate": False,
            },
        },
    }

# Configuración global del sistema de logging
def setup_logging():
    logging_config = get_logging_config()
    dictConfig(logging_config)
