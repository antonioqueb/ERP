import logging
from logging.config import dictConfig

logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        },
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "formatter": "default",
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "auth-service": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
    },
}

def setup_logging():
    dictConfig(logging_config)
