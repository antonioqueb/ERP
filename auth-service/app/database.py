from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://user:password@db-service:5432/gestpro_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear tablas si no existen (necesario para migraciones futuras)
from app.models.user import Base
Base.metadata.create_all(bind=engine)
