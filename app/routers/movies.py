from fastapi import APIRouter, Depends, Path, Query
from fastapi.responses import JSONResponse
from typing import List
from app.models.movie import Movie as MovieModel, MovieA as Movie
from app.utils.authentication import JWTBearer
from config.database import Session 

router = APIRouter()

# @router.get("/movies", tags=["movies"], response_model=List[Movie], status_code=200, dependencies=[Depends(JWTBearer())])
# def get_movies() -> List[Movie]:
#     return JSONResponse(status_code=200, content=movies)

# @router.get("/movies/{movie_id}", tags=["movies"], response_model=Movie, status_code=200, dependencies=[Depends(JWTBearer())])
# def get_movie(movie_id: int = Path(ge=1)) -> Movie:
#     for movie in movies:
#         if(movie["id"] == movie_id):
#             return JSONResponse(status_code=200, content=movie)
#     return JSONResponse(status_code=404, content=[])

# @router.get("/movies/", tags=["movies"], response_model=List[Movie], status_code=200, dependencies=[Depends(JWTBearer())])
# def get_movies_by_category(category: str = Query(None, min_length=3, max_length=50)) -> List[Movie]:
#     movie_list = []
#     for movie in movies:
#         categories = movie["category"].split("/")
#         if category in categories:
#             movie_list.append(movie)
#     return JSONResponse(status_code=200, content=movie_list)   

# @router.get("/moviesd/year/{movie_year}", tags=["movies"], response_model=List[Movie], status_code=200, dependencies=[Depends(JWTBearer())])
# def get_movies_by_year(movie_year: int = Path(le=2100, gt=1900)) -> List[Movie]:
#     movie_list = []
#     for movie in movies:
#         if(movie["year"] == movie_year):
#             movie_list.append(movie)
#     return JSONResponse(status_code=200, content=movie_list) 


@router.post("/movies", tags=["movies"], status_code=201)
def add_movie(movie: Movie):
    db = Session()
    new_movie_dict = vars(movie)
    new_movie = MovieModel(**new_movie_dict)
    db.add(new_movie)
    db.commit()
    return JSONResponse(status_code=201, content={"message": "Movie added successfully", "movie": new_movie_dict})

# @router.put("/movies/{movie_id}", tags=["movies"], status_code=200, dependencies=[Depends(JWTBearer())])
# def update_movie(movie_id: int, movie: Movie):
#     for movie in movies:
#         if(movie["id"] == movie_id):
#             movie["name"] = movie.name
#             movie["year"] = movie.year
#             movie["category"] = movie.category
#             movie["rating"] = movie.rating
#             return JSONResponse(status_code=200, content={"message": "Movie updated successfully"})
#     return JSONResponse(status_code=404, content=[])

# @router.delete("/movies/{movie_id}", tags=["movies"], status_code=200)
# def delete_movie(movie_id: int):
#     for movie in movies:
#         if(movie["id"] == movie_id):
#             movies.remove(movie)
#             return JSONResponse(status_code=200, content=movies)
#     return JSONResponse(status_code=404, content={})