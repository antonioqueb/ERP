import logging
from logging.config import dictConfig

# Configuración de logging dinámica basada en settings
def get_logging_config(settings):
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
                "level": settings.LOG_LEVEL,
                "formatter": "detailed" if settings.DEBUG else "default",
                "class": "logging.StreamHandler",
            },
            "file": {
                "level": settings.LOG_LEVEL,
                "formatter": "detailed",
                "class": "logging.FileHandler",
                "filename": settings.LOG_FILE,
            },
        },
        "loggers": {
            "gestpro-erp-core": {
                "handlers": ["console", "file"],
                "level": settings.LOG_LEVEL,
                "propagate": False,
            },
        },
    }

def setup_logging(settings):
    dictConfig(get_logging_config(settings))
