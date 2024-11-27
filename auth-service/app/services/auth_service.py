from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.user import User
from app.utils.token import verify_password, create_access_token

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def authenticate_user(db: Session, username: str, password: str):
    user = get_user_by_username(db, username)
    if user and verify_password(password, user.hashed_password):
        return user
    return None
