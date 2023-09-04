from fastapi import APIRouter, Depends, Path
from fastapi.responses import JSONResponse
from typing import List
from app.models.movie import Movie
from app.utils.authentication import JWTBearer

movies = [
    {"id": 1,"name": "The Godfather", "year": 1972, "category": "Crimen/Drama", "rating": 9.2},
    {"id": 2,"name": "The Shawshank Redemption", "year": 1994, "category": "Drama", "rating": 9.3},
    {"id": 3,"name": "Schindler's List", "year": 1993, "category": "Biography/Drama", "rating": 8.9},
]

router = APIRouter()

@router.get("/movies", tags=["movies"], response_model=List[Movie], status_code=200, dependencies=[Depends(JWTBearer())])
def get_movies() -> List[Movie]:
    return JSONResponse(status_code=200, content=movies)

@router.get("/movies/{movie_id}", tags=["movies"], response_model=Movie, status_code=200, dependencies=[Depends(JWTBearer())])
def get_movie(movie_id: int = Path(ge=1)) -> Movie:
    for movie in movies:
        if(movie["id"] == movie_id):
            return JSONResponse(status_code=200, content=movie)
    return JSONResponse(status_code=404, content=[])