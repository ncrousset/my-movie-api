from fastapi import FastAPI, Body, Path, Query
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
        json_schema_extra = {
            "example": {
                "name": "The Godfather",
                "year": 1972,
                "rating": 9.2
            }
        }

movies = [
    {"id": 1,"name": "The Godfather", "year": 1972, "category": "Crimen/Drama", "rating": 9.2},
    {"id": 2,"name": "The Shawshank Redemption", "year": 1994, "category": "Drama", "rating": 9.3},
    {"id": 3,"name": "Schindler's List", "year": 1993, "category": "Biography/Drama", "rating": 8.9},
]

@app.get("/", tags=["home"])
def read_root():
    return {"Hello": "World"}

@app.get("/movies", tags=["movies"])
def get_movies():
    return movies

@app.get("/movies/{movie_id}", tags=["movies"])
def get_movie(movie_id: int = Path(ge=1)):
    for movie in movies:
        if(movie["id"] == movie_id):
            return movie
    return []

@app.get("/movies/", tags=["movies"])
def get_movies_by_category(category: str = Query(None, min_length=3, max_length=50)):
    movie_list = []
    for movie in movies:
        if(movie["category"] == category):
            movie_list.append(movie)
    return movie_list       

@app.get("/movies/", tags=["movies"])
def get_movies_by_year(year: int = Path(le=2100, gt=1900)):
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

