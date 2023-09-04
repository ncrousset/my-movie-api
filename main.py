from fastapi import FastAPI, Body, Path, Query, Request, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi.security.http import HTTPAuthorizationCredentials
from pydantic import BaseModel, Field
from typing import Any, Coroutine, Optional, List

from starlette.requests import Request
from jwt_manager import create_token, validate_token
from fastapi.security import HTTPBearer

app = FastAPI()
app.title = "My movie API"
app.version = "0.0.1"

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data['email'] != "admin@email.com" and data['password'] != "admin":
            raise HTTPException(status_code=403, detail="Invalid username or password")    

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
    
class User(BaseModel):
    email: str
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "password": "password",
                "email": "johndoe@mail.com"
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

@app.post("/login", tags=["auth"])
def login(user: User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token = create_token(vars(user))
        return JSONResponse(status_code=200, content={"token": token})
    return JSONResponse(status_code=401, content={"message": "Unauthorized"})

@app.get("/movies", tags=["movies"], response_model=List[Movie], status_code=200, dependencies=[Depends(JWTBearer())])
def get_movies() -> List[Movie]:
    return JSONResponse(status_code=200, content=movies)

@app.get("/movies/{movie_id}", tags=["movies"], response_model=Movie, status_code=200)
def get_movie(movie_id: int = Path(ge=1)) -> Movie:
    for movie in movies:
        if(movie["id"] == movie_id):
            return JSONResponse(status_code=200, content=movie)
    return JSONResponse(status_code=404, content=[])

@app.get("/movies/category", tags=["movies"], response_model=List[Movie], status_code=200)
def get_movies_by_category(category: str = Query(None, min_length=3, max_length=50)) -> List[Movie]:
    movie_list = []
    for movie in movies:
        if(movie["category"] == category):
            movie_list.append(movie)
    return JSONResponse(status_code=200, content=movie_list)       

@app.get("/movies/", tags=["movies"], response_model=List[Movie], status_code=200)
def get_movies_by_year(year: int = Path(le=2100, gt=1900)) -> List[Movie]:
    movie_list = []
    for movie in movies:
        if(movie["year"] == year):
            movie_list.append(movie)
    return JSONResponse(status_code=200, content=movie_list)

@app.post("/movies", tags=["movies"], status_code=201)
def add_movie(movie: Movie):
    movies.append(movie)
    return JSONResponse(status_code=201, content={"message": "Movie added successfully"})

@app.put("/movies/{movie_id}", tags=["movies"], status_code=200)
def update_movie(movie_id: int, movie: Movie):
    for movie in movies:
        if(movie["id"] == movie_id):
            movie["name"] = movie.name
            movie["year"] = movie.year
            movie["rating"] = movie.rating
            return JSONResponse(status_code=200, content=movie)
    return JSONResponse(status_code=404, content=[])

@app.delete("/movies/{movie_id}", tags=["movies"], status_code=200)
def delete_movie(movie_id: int):
    for movie in movies:
        if(movie["id"] == movie_id):
            movies.remove(movie)
            return JSONResponse(status_code=200, content=movies)
    return JSONResponse(status_code=404, content={})