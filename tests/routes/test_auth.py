from tests.test_main import test_db_init, client, get_token
def test_auth_login(client, test_db_init):
    headers = {'Content-Type': 'application/json'}
    response = client.post(
        "/login",
        json={"email": "test@test.com", "password": "password"},
        headers=headers
    )

    assert response.status_code == 200
    assert response.json()["token"] is not None

def test_auth_login_invalid_credentials(client, test_db_init):
    headers = {'Content-Type': 'application/json'}
    response = client.post(
        "/login",
        json={"email": "tito@macana.com", "password": "password"},
        headers=headers
    )

    assert response.status_code == 404
    assert response.json()["message"] == "User not found"


def test_auth_login_invalid_password(client, test_db_init):
    headers = {'Content-Type': 'application/json'}
    response = client.post(
        "/login",
        json={"email": "test@test.com", "password": "wrongpassword"},
        headers=headers
    )

    assert response.status_code == 401
    assert response.json()["message"] == "Unauthorized"