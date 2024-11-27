from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Gestpro-ERP Auth Service"
    ENVIRONMENT: str = "development"
    API_VERSION: str = "/api/v1"
    SECRET_KEY: str = "your-secret-key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    DATABASE_SERVICE_URL: str = "http://db-service:8001/api/v1"

    class Config:
        env_file = ".env"

settings = Settings()
