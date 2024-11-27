from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Gestpro-ERP Core"
    ENVIRONMENT: str = "development"
    DATABASE_SERVICE_URL: str = "http://db-service:8001/api/v1"
    AUTH_SERVICE_URL: str = "http://auth-service:8002/api/v1"
    API_VERSION: str = "/api/v1"



    class Config:
        env_file = ".env"

# Instancia global de settings
settings = Settings()
