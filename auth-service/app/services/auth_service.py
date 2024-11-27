from app.utils.token import verify_password

# Simulación de una base de datos de usuarios
fake_users_db = {
    "admin": {
        "username": "admin",
        "hashed_password": "$2b$12$eIX/gOxlP.xNvLPwVFRHNOcFCtCZB5WQG4R1t5j6lfYB61Zm1S6nG",  # Hash de "password"
    }
}

def authenticate_user(username: str, password: str):
    """
    Autentica un usuario contra la base de datos simulada.
    """
    user = fake_users_db.get(username)
    if user and verify_password(password, user["hashed_password"]):
        return user
    return None
