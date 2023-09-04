from fastapi import FastAPI, Body
from pydantic import BaseModel, Field

app = FastAPI()
app.title = "My movie API"
app.version = "0.0.1"

class Movie(BaseModel):
    id: int
    name: str = Field(..., max_length=50)
    year: int = Field(..., gt=1900, lt=2100)
    rating: float = Field(...,le=10, ge=0)

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "name": "The Godfather",
                "year": 1972,
                "rating": 9.2
            }
        }

movies = [
    {"id": 1,"name": "The Godfather", "year": 1972, "rating": 9.2},
    {"id": 2, "name": "The Shawshank Redemption", "year": 1994, "rating": 9.3},
    {"id": 3, "name": "Schindler's List", "year": 1994, "rating": 8.9},
    {"id": 4, "name": "Raging Bull", "year": 1980, "rating": 8.2},
    {"id": 5, "name": "Casablanca", "year": 1942, "rating": 8.5},
    {"id": 6, "name": "Citizen Kane", "year": 1941, "rating": 8.3},
    {"id": 7, "name": "Gone with the Wind", "year": 1939, "rating": 8.1},
    {"id": 8, "name": "The Wizard of Oz", "year": 1939, "rating": 8},
    {"id": 9, "name": "One Flew Over the Cuckoo's Nest", "year": 1975, "rating": 8.7},
    {"id": 10, "name": "Lawrence of Arabia", "year": 1962, "rating": 8.3},
    {"id": 11, "name": "Vertigo", "year": 1958, "rating": 8.3},
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

@app.get("/movies/", tags=["movies"])
def get_movies_by_year(year: int):
    movie_list = []
    for movie in movies:
        if(movie["year"] == year):
            movie_list.append(movie)
    return movie_list

@app.post("/movies", tags=["movies"])
def add_movie(movie: Movie):
    movies.append(movie)
    return movies

@app.put("/movies/{movie_id}", tags=["movies"])
def update_movie(movie_id: int, movie: Movie):
    for movie in movies:
        if(movie["id"] == movie_id):
            movie["name"] = movie.name
            movie["year"] = movie.year
            movie["rating"] = movie.rating
            return movie
    return []

@app.delete("/movies/{movie_id}", tags=["movies"])
def delete_movie(movie_id: int):
    for movie in movies:
        if(movie["id"] == movie_id):
            movies.remove(movie)
            return movies
    return []