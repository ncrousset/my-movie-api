from tests.test_main import client, get_token

post_data = {
        "title": "The Godfather",
        "year": 1972,
        "director": "Francis Ford Coppola",
        "imdb_rating": 9.2,
        "categories": [
            {"id": 1, "name": "Action"},
            {"id": 2, "name": "Adventure"},
            {"id": 3, "name": "Animation"}
        ],
}


def test_create_movie(client, get_token):
    """
    Test the creation of a movie using an authentication JWT token.
    """
    # TODO: Agregar la categoria
    headers = {"Authorization": "Bearer " + get_token, 'Content-Type': 'application/json'}
    response = client.post(
        "/movie",
        json=post_data,
        headers=headers
    )
    assert response.status_code == 201

def test_create_movie_unauthenticated(client):
    """
    Test the creation of a movie without an authentication JWT token.

    Verifies that a POST request to '/movie' without an authenticated user's JWT token
    returns a status code of 401 (Unauthorized).
    """
    headers = {'Content-Type': 'application/json'}
    response = client.post(
        "/movie",
        json=post_data,
        headers=headers
    )
    assert response.status_code == 403

def test_create_movie_invalid_data(client, get_token):
    """
    Test the creation of a movie with invalid data using an authentication JWT token.

    Verifies that a POST request to '/movie' with an authenticated user's JWT token
    and invalid data returns a status code of 422 (Unprocessable Entity).
    """
    headers = {"Authorization": "Bearer " + get_token, 'Content-Type': 'application/json'}
    response = client.post(
        "/movie",
        json={"title": "The Godfather"},
        headers=headers
    )
    assert response.status_code == 422

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
    assert type(response.json()[0]['id']) == int

def test_get_movies_unauthenticated(client):
    """
    Test retrieving a movie by its ID without authentication.

    Verifies that a GET request to '/movie/1' without an authenticated user's JWT token
    returns a status code of 401 (Unauthorized).
    """
    response = client.get('/movies')
    assert response.status_code == 403

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
    assert response.json()['id'] == 1

def test_get_movie_unauthenticated(client):
    """
    Test retrieving a movie by its ID without authentication.

    Verifies that a GET request to '/movie/1' without an authenticated user's JWT token
    returns a status code of 401 (Unauthorized).
    """
    response = client.get('/movie/1')
    assert response.status_code == 403


# TODO: Activar test de category
def test_get_movies_by_category(client, get_token):
    """Test retrieving movies by category with authentication using a JWT token.

    Verifies that a GET request to '/movies/?category=Crime' with an authenticated
    user's JWT token returns a status code of 200 (OK) and checks that the title of
    the first movie in the response matches the expected title.
    """
    headers = {"Authorization": "Bearer " + get_token}
    response = client.get("/movies/?category=Action", headers=headers)

    assert response.status_code == 200
    assert type(response.json()[0]['id']) == int and response.json()[0]['id'] > 0

def test_get_movies_by_category_unauthenticated(client):
    """Test retrieving movies by category without authentication.

    Verifies that a GET request to '/movies/?category=Crime' without an authenticated
    user's JWT token returns a status code of 401 (Unauthorized).
    """
    response = client.get("/movies/?category=Action")
    assert response.status_code == 403

def test_get_movies_by_category_invalid_category(client, get_token):
    headers = {"Authorization": "Bearer " + get_token}
    response = client.get("/movies/?category=NoExixste", headers=headers)

    assert response.status_code == 404
    assert response.json()['message'] == "Movie not found"

def test_update_movie(client, get_token):
    """Test updating a movie's category with authentication using a JWT token.

    Appends "Comedy" to the movie's category and sends a PUT request to '/movie/1'
    with an authenticated user's JWT token. Verifies that the response status code
    is 200 (OK).
    """
    post_data['director'] += "Hola"
    headers = {"Authorization": "Bearer " + get_token, 'Content-Type': 'application/json'}
    response = client.put(
        "/movie/3",
        json=post_data,
        headers=headers
    )
    assert response.status_code == 200

def test_update_movie_unauthenticated(client):
    """Test updating a movie's category without authentication.

    Appends "Comedy" to the movie's category and sends a PUT request to '/movie/1'
    without an authenticated user's JWT token. Verifies that the response status code
    is 401 (Unauthorized).
    """
    post_data['director'] += "hola"
    headers = {'Content-Type': 'application/json'}
    response = client.put(
        "/movie/3",
        json=post_data,
        headers=headers
    )
    assert response.status_code == 403

def test_update_movie_invalid_data(client, get_token):
    headers = {"Authorization": "Bearer " + get_token, 'Content-Type': 'application/json'}
    response = client.put(
        "/movie/3",
        headers=headers
    )
    assert response.status_code == 422

def test_delete_movie(client, get_token):
    """Test deleting a movie with authentication using a JWT token.

    Sends a DELETE request to '/movie/1' with an authenticated user's JWT token.
    """
    headers = {"Authorization": "Bearer " + get_token, 'Content-Type': 'application/json'}
    response = client.delete(
        "/movie/2",
        headers=headers
    )
    assert response.status_code == 200

def test_delete_movie_unauthenticated(client):
    """Test deleting a movie without authentication.

    Sends a DELETE request to '/movie/1' without an authenticated user's JWT token.
    Verifies that the response status code is 401 (Unauthorized).
    """
    headers = {'Content-Type': 'application/json'}
    response = client.delete(
        "/movie/2",
        headers=headers
    )
    assert response.status_code == 403
