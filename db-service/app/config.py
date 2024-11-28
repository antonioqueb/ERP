from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    project_name: str = "Gestpro-ERP Database Service"
    environment: str = Field(default="development")
    api_version: str = Field(default="/api/v1", env="API_VERSION")
    database_url: str = Field(..., env="DATABASE_URL")

    class Config:
        env_file = ".env"

settings = Settings()
