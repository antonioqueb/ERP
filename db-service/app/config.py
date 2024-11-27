# db-service/app/config.py

from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Gestpro-ERP Database Service"
    ENVIRONMENT: str = "development"
    API_VERSION: str = "/api/v1"

    class Config:
        env_file = ".env"

settings = Settings()
