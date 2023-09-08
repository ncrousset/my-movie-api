from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session
# from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from app.middlewares.jwt_bearer import JWTBearer
from app.services.movie import MovieService
from app.schemas.movie import Movie

router = APIRouter()


@router.get("/movies", tags=["movies"], response_model=List[Movie], status_code=200, dependencies=[Depends(JWTBearer())]) 
def get_movies() -> List[Movie]:
    db = Session()
    result = MovieService(db).get_movies()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@router.get("/movie/{movie_id}", tags=["movies"], response_model=Movie, status_code=200)    
def get_movie(movie_id: int) -> Movie:
    db = Session()
    result = MovieService(db).get_movie(movie_id)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@router.get("/movies/", tags=["movies"], response_model=List[Movie], status_code=200)
def get_movies_by_category(category: str = Query(None, min_length=3, max_length=50)) -> List[Movie]:
    db = Session()
    movies = MovieService(db).get_movies_by_category(category)
    if not movies:
        return JSONResponse(status_code=404, content={"message": "Movie not found"})
    return JSONResponse(status_code=200, content=jsonable_encoder(movies))

@router.post("/movie", tags=["movies"], response_model=Movie, status_code=201)  
def create_movie(movie: Movie) -> Movie:
    db = Session()
    result = MovieService(db).create_movie(movie)
    return JSONResponse(status_code=201, content=jsonable_encoder(result))

@router.put("/movie/{movie_id}", tags=["movies"], response_model=Movie, status_code=200)
def update_movie(movie_id: int, movie: Movie) -> Movie:
    db = Session()
    result = MovieService(db).update_movie(movie_id, movie)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@router.delete("/movie/{movie_id}", tags=["movies"], response_model=Movie, status_code=200)
def delete_movie(movie_id: int) -> Movie:
    db = Session()
    result = MovieService(db).delete_movie(movie_id)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))