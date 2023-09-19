import pytest
from fastapi.testclient import TestClient
from main import app
from app.schemas.user import User
from app.utils.jwt_manager import create_token

# add user and son information need to run this test
import populates

populates.run()

USER_FAKE_EMAIL = "test@gmail.com"
USER_FAKE_PASS = "123456"

@pytest.fixture(scope="session")
def client():
    return TestClient(app)

@pytest.fixture(scope="session")
def get_token(client):
    user = User.Auth(
        email=USER_FAKE_EMAIL,
        password=USER_FAKE_PASS
    )

    token = create_token(vars(user))

    return token

