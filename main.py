from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List


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
                "id": 1,
                "name": "The Godfather",
                "year": 1972,
                "rating": 9.2
            }
        }

    def __str__(self):
        return f"{self.id} - {self.name} - {self.year} - {self.rating}"
    

movies = [
    {"id": 1,"name": "The Godfather", "year": 1972, "category": "Crimen/Drama", "rating": 9.2},
    {"id": 2,"name": "The Shawshank Redemption", "year": 1994, "category": "Drama", "rating": 9.3},
    {"id": 3,"name": "Schindler's List", "year": 1993, "category": "Biography/Drama", "rating": 8.9},
]

@app.get("/", tags=["home"])
def read_root():
    return {"Hello": "World"}

@app.get("/movies", tags=["movies"], response_model=List[Movie])
def get_movies() -> List[Movie]:
    return JSONResponse(content=movies)

@app.get("/movies/{movie_id}", tags=["movies"], response_model=Movie)
def get_movie(movie_id: int = Path(ge=1)) -> Movie:
    for movie in movies:
        if(movie["id"] == movie_id):
            return JSONResponse(content=movie)
    return JSONResponse(content=[])

@app.get("/movies/category", tags=["movies"], response_model=List[Movie])
def get_movies_by_category(category: str = Query(None, min_length=3, max_length=50)) -> List[Movie]:
    movie_list = []
    for movie in movies:
        if(movie["category"] == category):
            movie_list.append(movie)
    return JSONResponse(content=movie_list)       

@app.get("/movies/", tags=["movies"], response_model=List[Movie])
def get_movies_by_year(year: int = Path(le=2100, gt=1900)) -> List[Movie]:
    movie_list = []
    for movie in movies:
        if(movie["year"] == year):
            movie_list.append(movie)
    return JSONResponse(content=movie_list)

@app.post("/movies", tags=["movies"])
def add_movie(movie: Movie):
    movies.append(movie)
    return JSONResponse(content={"message": "Movie added successfully"})

@app.put("/movies/{movie_id}", tags=["movies"])
def update_movie(movie_id: int, movie: Movie):
    for movie in movies:
        if(movie["id"] == movie_id):
            movie["name"] = movie.name
            movie["year"] = movie.year
            movie["rating"] = movie.rating
            return JSONResponse(content=movie)
    return JSONResponse(content=[])

@app.delete("/movies/{movie_id}", tags=["movies"])
def delete_movie(movie_id: int):
    for movie in movies:
        if(movie["id"] == movie_id):
            movies.remove(movie)
            return JSONResponse(content=movies)
    return JSONResponse(content={})