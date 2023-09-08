import jwt
from app.schemas.user import User
from datetime import datetime, timedelta
from app.utils.jwt_manager import create_token
from app.models.user import User as UserModel
from config.database import Session_test


def create_jwt_token(user: User, expires_in_minutes: int = 60):
    expire = datetime.utcnow() + timedelta(minutes=expires_in_minutes)
    data: dict = {"exp": expire, "user_id": user.id, "username": user.username}
    token: str = create_token(data)
    return token

def get_jwt_token(expires_in_minutes: int = 60):
    user = create_user()
    token = create_jwt_token(user, expires_in_minutes)
    return token

def create_user():
    db = Session_test()
    user = {
        "email": "test@gmail.com",
        "password": "password"
    }

    user = UserModel(user)
    db.add(user)
    db.commit()

    return user

