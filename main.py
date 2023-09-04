from fastapi import FastAPI # Body, Path, Query, Request, Depends, HTTPException
from app.routers import movies as movies_router
from app.routers import auth as auth_router
# from fastapi.responses import JSONResponse
# from fastapi.security.http import HTTPAuthorizationCredentials
# from pydantic import BaseModel, Field
# from typing import Any, Coroutine, Optional, List

# from starlette.requests import Request
# from jwt_manager import create_token, validate_token
# 

app = FastAPI()
app.title = "My movie API"
app.version = "0.0.1"

app.include_router(auth_router.router)
app.include_router(movies_router.router)


# @app.get("/", tags=["home"])
# def read_root():
#     return {"Hello": "World"}







# @app.get("/movies/category", tags=["movies"], response_model=List[Movie], status_code=200)
# def get_movies_by_category(category: str = Query(None, min_length=3, max_length=50)) -> List[Movie]:
#     movie_list = []
#     for movie in movies:
#         if(movie["category"] == category):
#             movie_list.append(movie)
#     return JSONResponse(status_code=200, content=movie_list)       

# @app.get("/movies/", tags=["movies"], response_model=List[Movie], status_code=200)
# def get_movies_by_year(year: int = Path(le=2100, gt=1900)) -> List[Movie]:
#     movie_list = []
#     for movie in movies:
#         if(movie["year"] == year):
#             movie_list.append(movie)
#     return JSONResponse(status_code=200, content=movie_list)

# @app.post("/movies", tags=["movies"], status_code=201)
# def add_movie(movie: Movie):
#     movies.append(movie)
#     return JSONResponse(status_code=201, content={"message": "Movie added successfully"})

# @app.put("/movies/{movie_id}", tags=["movies"], status_code=200)
# def update_movie(movie_id: int, movie: Movie):
#     for movie in movies:
#         if(movie["id"] == movie_id):
#             movie["name"] = movie.name
#             movie["year"] = movie.year
#             movie["rating"] = movie.rating
#             return JSONResponse(status_code=200, content=movie)
#     return JSONResponse(status_code=404, content=[])

# @app.delete("/movies/{movie_id}", tags=["movies"], status_code=200)
# def delete_movie(movie_id: int):
#     for movie in movies:
#         if(movie["id"] == movie_id):
#             movies.remove(movie)
#             return JSONResponse(status_code=200, content=movies)
#     return JSONResponse(status_code=404, content={})