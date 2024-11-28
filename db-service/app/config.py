# db-service/app/config.py

from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    PROJECT_NAME: str = "Gestpro-ERP Database Service"
    ENVIRONMENT: str = "development"
    API_VERSION: str = "/api/v1"
    database_url: str = Field(..., env='DATABASE_URL')

    class Config:
        env_file = ".env"

settings = Settings()
