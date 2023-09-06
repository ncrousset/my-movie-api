from fastapi import APIRouter, Depends, Path, Query
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List
from app.models.movie import Movie as MovieModel, Pato as Movie 
from app.middlewares.jwt_bearer import JWTBearer
from config.database import Session 
from app.services.movie import MovieService

router = APIRouter()

@router.get("/movies", tags=["movies"], response_model=Movie, status_code=200, dependencies=[Depends(JWTBearer())])
def get_movies() -> Movie:
    db = Session()
    result = MovieService(db).get_movies()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@router.get("/movies/{movie_id}", tags=["movies"], response_model=Movie, status_code=200, dependencies=[Depends(JWTBearer())])
def get_movie(movie_id: int = Path(ge=1)) -> Movie:
    db = Session()
    result = MovieService(db).get_movie_by_id(movie_id)   
    if not result:
        return JSONResponse(status_code=404, content={"message": "Movie not found"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@router.get("/movies/", tags=["movies"], response_model=List[Movie], status_code=200)
def get_movies_by_category(category: str = Query(None, min_length=3, max_length=50)) -> List[Movie]:
    db = Session()
    movies = MovieService(db).get_movies_by_category(category)
    if not movies:
        return JSONResponse(status_code=404, content={"message": "Movie not found"})
    return JSONResponse(status_code=200, content=jsonable_encoder(movies))

@router.get("/moviesd/year/{movie_year}", tags=["movies"], response_model=List[Movie], status_code=200)
def get_movies_by_year(movie_year: int = Path(le=2100, gt=1900)) -> List[Movie]:
    db = Session()
    result = MovieService(db).get_movies_by_year(movie_year)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Movie not found"})    
    return JSONResponse(status_code=200, content=jsonable_encoder(result)) 

@router.post("/movies", tags=["movies"], status_code=201, dependencies=[Depends(JWTBearer())])
def add_movie(movie: Movie):
    db = Session()
    result = MovieService(db).create_movie(movie)
    return JSONResponse(status_code=201, content={"message": "Movie added successfully"})

@router.put("/movies/{movie_id}", tags=["movies"], status_code=200, dependencies=[Depends(JWTBearer())])
def update_movie(movie_id: int, movie: Movie):
    db = Session()
    result = MovieService(db).update_movie(movie_id, movie)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Movie not found"})
    return JSONResponse(status_code=200, content={"message": "Movie updated successfully"})
    
@router.delete("/movies/{movie_id}", tags=["movies"], status_code=200, dependencies=[Depends(JWTBearer())])
def delete_movie(movie_id: int):
    db = Session()
    result = MovieService(db).delete(movie_id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Movie not found"})
    return JSONResponse(status_code=200, content={"message": "Movie deleted successfully"}) 