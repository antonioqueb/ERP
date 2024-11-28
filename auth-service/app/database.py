from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings  # Importa las configuraciones

engine = create_engine(settings.database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear tablas si no existen (necesario para migraciones futuras)
from app.models.user import Base
Base.metadata.create_all(bind=engine)
