from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.database import SessionLocal
from app.models.user import User
from app.utils.token import verify_password, create_access_token

def get_user_by_username(db: Session, username: str) -> User:
    """
    Obtiene un usuario de la base de datos según su nombre de usuario.

    Args:
        db (Session): Sesión de base de datos.
        username (str): Nombre de usuario.

    Returns:
        User: Objeto del usuario si existe, None en caso contrario.
    """
    try:
        return db.query(User).filter(User.username == username).first()
    except SQLAlchemyError as e:
        # Manejo de errores en consultas
        raise RuntimeError(f"Error al consultar el usuario: {e}")

def authenticate_user(db: Session, username: str, password: str) -> User:
    """
    Autentica a un usuario verificando su contraseña.

    Args:
        db (Session): Sesión de base de datos.
        username (str): Nombre de usuario.
        password (str): Contraseña sin hashear.

    Returns:
        User: Objeto del usuario autenticado si las credenciales son correctas.
        None: Si las credenciales no son válidas.
    """
    user = get_user_by_username(db, username)
    if user and verify_password(password, user.hashed_password):
        return user
    return None
