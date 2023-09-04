from fastapi import FastAPI

app = FastAPI()
app.title = "My movie API"
app.version = "0.0.1"

movies = [
    {"id": 1,"name": "The Godfather", "year": 1972, "rating": 9.2},
    {"id": 2, "name": "The Shawshank Redemption", "year": 1994, "rating": 9.3},
    {"id": 3, "name": "Schindler's List", "year": 1993, "rating": 8.9},
]

@app.get("/", tags=["home"])
def read_root():
    return {"Hello": "World"}

@app.get("/movies", tags=["movies"])
def get_movies():
    return movies

@app.get("/movies/{movie_id}", tags=["movies"])
def get_movie(movie_id: int):
    for movie in movies:
        if(movie["id"] == movie_id):
            return movie
    return []