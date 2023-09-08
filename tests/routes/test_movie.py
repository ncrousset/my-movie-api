import pytest
from tests.test_main import test_db, client, create_user, get_token
from app.models.user import User as UserModel
import json


post_data = {
        "title": "The Godfather",
        "year": 1972,
        "category": "Crime, Drama2",
        "director": "Francis Ford Coppola",
        "imdb_rating": 9.2
}

def test_create_movie(client, get_token):
    headers = {"Authorization": "Bearer " + get_token, 'Content-Type': 'application/json'}

    response = client.post(
        "/movie",
        json=post_data,
        headers=headers
    )

    assert response.status_code == 201

def test_get_movies(client, get_token):
    headers = {"Authorization": "Bearer " + get_token}

    response = client.get('/movies', headers=headers)

    assert response.status_code == 200
    assert response.json()[0]['title'] == post_data['title']
