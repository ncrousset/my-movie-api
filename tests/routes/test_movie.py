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
    """
    Test the creation of a movie using an authentication JWT token.
    """
    headers = {"Authorization": "Bearer " + get_token, 'Content-Type': 'application/json'}
    response = client.post(
        "/movie",
        json=post_data,
        headers=headers
    )
    assert response.status_code == 201

def test_get_movies(client, get_token):
    """
    Test retrieving movies with authentication using a JWT token.

    Verifies that a GET request to '/movies' with an authenticated user's JWT token
    returns a status code of 200 (OK) and checks that the title of the first movie in
    the response matches the expected title.
    """
    headers = {"Authorization": "Bearer " + get_token}
    response = client.get('/movies', headers=headers)
    assert response.status_code == 200
    assert response.json()[0]['title'] == post_data['title']

def test_get_movie(client, get_token):
    """
    Test retrieving a movie by its ID using authentication with a JWT token.

    Verifies that a GET request to '/movie/1' with an authenticated user's JWT token
    returns a status code of 200 (OK) and checks that the title of the retrieved movie
    matches the expected title.
    """
    headers = {"Authorization": "Bearer " + get_token}
    response = client.get('/movie/1', headers=headers)
    assert response.status_code == 200
    assert response.json()['title'] == post_data['title']

def test_get_movies_by_category(client, get_token):
    """Test retrieving movies by category with authentication using a JWT token.

    Verifies that a GET request to '/movies/?category=Crime' with an authenticated
    user's JWT token returns a status code of 200 (OK) and checks that the title of
    the first movie in the response matches the expected title.
    """
    headers = {"Authorization": "Bearer " + get_token}
    response = client.get("/movies/?category=Crime", headers=headers)
    assert response.status_code == 200
    assert response.json()[0]['title'] == post_data['title']