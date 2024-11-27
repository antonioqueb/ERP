from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Configuración general
    PROJECT_NAME: str = "Gestpro-ERP Auth Service"
    ENVIRONMENT: str = "development"
    API_VERSION: str = "/api/v1"
    
    # Configuración de seguridad
    SECRET_KEY: str = "your-secret-key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Configuración de la base de datos
    DATABASE_URL: str  # Declaración de la variable para la URL de la base de datos

    class Config:
        env_file = ".env"  # Cargar variables desde el archivo .env

# Instancia global de configuración
settings = Settings()
