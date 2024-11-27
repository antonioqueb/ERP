from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Gestpro-ERP Auth Service"
    ENVIRONMENT: str = "development"
    API_VERSION: str = "/api/v1"
    SECRET_KEY: str  # Será obligatorio configurarlo en `.env`
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    DATABASE_URL: str  # Será obligatorio configurarlo en `.env`
    AUTH_SERVICE_URL: str = "http://auth-service:8002/api/v1"

    class Config:
        env_file = ".env"  # Carga valores desde un archivo .env

# Instanciar la configuración
settings = Settings()
