import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.database import Base, Session
from fastapi.testclient import TestClient
from main import app
from app.models.user import User as UserModel
from tests.utils import get_jwt_token


@pytest.fixture(scope="session")
def test_db():
    engine = create_engine("sqlite:///:memory:")
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)
    yield TestingSessionLocal()
    engine.dispose()

@pytest.fixture(scope="session")
def client(test_db):
    return TestClient(app)

@pytest.fixture(scope="session")
def create_user(test_db):
    with test_db as db:
        user = UserModel(email="test@gmail.com", password="password")
        db.add(user)
    return user

@pytest.fixture(scope="session")
def get_token(create_user):
    token = get_jwt_token(create_user)
    return token
