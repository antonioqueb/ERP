from app.utils.token import verify_password, create_access_token

# Simulated user database
fake_users_db = {
    "admin": {
        "username": "admin",
        "hashed_password": "$2b$12$eIX/gOxlP.xNvLPwVFRHNOcFCtCZB5WQG4R1t5j6lfYB61Zm1S6nG",  # Hash of "password"
    }
}

def authenticate_user(username: str, password: str):
    user = fake_users_db.get(username)
    if user and verify_password(password, user["hashed_password"]):
        return user
    return None

__all__ = ['authenticate_user', 'create_access_token']
