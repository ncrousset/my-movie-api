from tests.test_main import test_db_init, client, get_token, USER_FAKE_EMAIL

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
        "/user/30000"
    )

    assert response.status_code == 404
    assert response.json()["message"] == "User not found"

