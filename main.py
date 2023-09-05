from fastapi import FastAPI # Body, Path, Query, Request, Depends, HTTPException
from app.routers import movies as movies_router
# from app.routers import auth as auth_router
from config.database import engine, Session, Base
from app.models.movie import Movie as MovieModel


app = FastAPI()
app.title = "My movie API"
app.version = "0.0.1"

Base.metadata.create_all(bind=engine)

# app.include_router(auth_router.router)
app.include_router(movies_router.router)


# @app.get("/", tags=["home"])
# def read_root():
#     return {"Hello": "World"}
