from tests.test_main import client, USER_FAKE_EMAIL, USER_FAKE_PASS
def test_auth_login(client):
    headers = {'Content-Type': 'application/json'}
    response = client.post(
        "/login",
        json={"email": USER_FAKE_EMAIL, "password": USER_FAKE_PASS},
        headers=headers
    )

    assert response.status_code == 200
    assert response.json()["token"] is not None

def test_auth_login_invalid_credentials(client):
    headers = {'Content-Type': 'application/json'}
    response = client.post(
        "/login",
        json={"email": "tito@macana.com", "password": "password"},
        headers=headers
    )

    assert response.status_code == 401
    assert response.json()["message"] == "User not found"


def test_auth_login_invalid_password(client):
    headers = {'Content-Type': 'application/json'}
    response = client.post(
        "/login",
        json={"email": USER_FAKE_EMAIL, "password": "wrongpassword"},
        headers=headers
    )

    assert response.status_code == 401
    assert response.json()["message"] == "Unauthorized"