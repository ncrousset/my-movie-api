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
