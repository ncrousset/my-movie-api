from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from typing import List
from app.models.movie import Movie

movies = [
    {"id": 1,"name": "The Godfather", "year": 1972, "category": "Crimen/Drama", "rating": 9.2},
    {"id": 2,"name": "The Shawshank Redemption", "year": 1994, "category": "Drama", "rating": 9.3},
    {"id": 3,"name": "Schindler's List", "year": 1993, "category": "Biography/Drama", "rating": 8.9},
]

router = APIRouter()

@router.get("/movies", tags=["movies"], response_model=List[Movie], status_code=200)
def get_movies() -> List[Movie]:
    return JSONResponse(status_code=200, content=movies)