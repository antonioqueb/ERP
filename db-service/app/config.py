from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    project_name: str = "Gestpro-ERP Database Service"
    environment: str = "development"
    api_version: str = "/api/v1"
    database_url: str = Field(..., env='DATABASE_URL')

    model_config = {
        "env_file": ".env",
    }

settings = Settings()
