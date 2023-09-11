from tests.test_main import test_db_init, client, get_token, USER_FAKE_EMAIL
from faker import Faker

fake = Faker()

def test_get_user(client, get_token):
    headers = {"Authorization": "Bearer " + get_token, 'Content-Type': 'application/json'}
    response = client.get(
        "/user/1",
        headers=headers
    )

    assert response.status_code == 200
    assert response.json()["email"] == USER_FAKE_EMAIL

def test_get_user_unauthenticated(client):
    response = client.get(
        "/user/1"
    )

    assert response.status_code == 403
    assert response.json()["detail"] == "Not authenticated"


def test_get_user_not_found(client, get_token):
    headers = {"Authorization": "Bearer " + get_token, 'Content-Type': 'application/json'}
    response = client.get(
        "/user/3000",
        headers=headers
    )

    assert response.status_code == 404
    assert response.json()["message"] == "User not found"

def test_register_user(client):
    headers = {'Content-Type': 'application/json'}

    data = {
        "name": "Test",
        "email": fake.email(True, "gmail.com"),
        "password": "password"
    }

    response = client.post(
        "/user",
        json=data,
        headers=headers
    )

    assert response.status_code == 201
    # assert response.json()["token"] is not None

def test_register_user_invalid_email(client):
    headers = {'Content-Type': 'application/json'}
    data = {
        "name": "Test",
        "email": "test",
        "password": "password"
    }

    response = client.post(
        "/user",
        json=data,
        headers=headers
    )

    assert response.status_code == 422

def test_register_user_already_exists(client, test_db_init):
    data = {
        "name": "Test",
        "email": USER_FAKE_EMAIL,
        "password": "password"
    }

    headers = {'Content-Type': 'application/json'}
    response = client.post(
        "/user",
        json=data,
        headers=headers
    )

    assert response.status_code == 400
    assert response.json()["message"] == "User already exists"