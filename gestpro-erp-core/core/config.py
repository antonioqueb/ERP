from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Gestpro-ERP Core"
    ENVIRONMENT: str = "development"
    DATABASE_SERVICE_URL: str = "http://db-service:8001/api/v1"
    AUTH_SERVICE_URL: str = "http://auth-service:8002/api/v1"
    API_VERSION: str = "/api/v1"

    # Configuración de logs
    LOG_LEVEL: str = Field(default="INFO", env="LOG_LEVEL")
    LOG_FILE: str = Field(default="gestpro-erp-core.log", env="LOG_FILE")
    DEBUG: bool = Field(default=True, env="DEBUG")
    TIMEOUT: int = Field(default=30, env="TIMEOUT")

    class Config:
        env_file = ".env"

# Instancia global de settings
settings = Settings()
