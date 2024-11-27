from app.utils.db_client import DatabaseClient
from app.utils.token import verify_password

db_client = DatabaseClient()

async def authenticate_user(username: str, password: str):
    try:
        user = await db_client.get_user(username)
        if user and verify_password(password, user["hashed_password"]):
            return user
    except Exception as e:
        # Manejar errores, como usuario no encontrado o problema de conexión
        return None
    return None
