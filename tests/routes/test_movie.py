from fastapi.testclient import TestClient
from main import app
from config.database import Session_test
from tests.test_utilities import get_jwt_token

client = TestClient(app)


def test_get_movies():

    token = get_jwt_token()
    print(token)

    response = client.get("/movies")
    assert response.status_code == 200
