import pytest
from config.database import Base, Session
from fastapi.testclient import TestClient
from main import app
from app.models.user import User as UserModel
from app.schemas.user import User
from tests.utils import get_jwt_token
from app.services.user import UserService
from app.utils.jwt_manager import create_token


USER_FAKE_EMAIL = "test@test.com"
USER_FAKE_PASS = "password"

@pytest.fixture(scope="session")
def test_db_init():
    db = Session()
    register_user = UserModel(
        name="Test",
        email=USER_FAKE_EMAIL,
        password=USER_FAKE_PASS,
    )

    user = UserService(db).get_user_by_email(register_user.email)

    if not user:
        db.add(register_user)
        db.commit()


@pytest.fixture(scope="session")
def client(test_db_init):
    return TestClient(app)


@pytest.fixture(scope="session")
def get_token(client):
    user = User.Auth(
        email=USER_FAKE_EMAIL,
        password=USER_FAKE_PASS
    )

    token = create_token(vars(user))

    return token

