import jwt
from app.schemas.user import User
from datetime import datetime, timedelta
from app.utils.jwt_manager import create_token


def create_jwt_token(user: User, expires_in_minutes: int = 60):
    expire = datetime.utcnow() + timedelta(minutes=expires_in_minutes)
    data: dict = {"exp": expire, "user_id": user.id, "email": user.email}
    token: str = create_token(data)
    return token

def get_jwt_token(user, expires_in_minutes: int = 60):
    token = create_jwt_token(user, expires_in_minutes)
    return token

def create_fake_movie():
    return {
        "title": "Test Movie",
        "description": "Test Description",
        "genre": "Test Genre",
        "owner": 1
    }