from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from app.models.user import User
from app.utils.jwt_manager import create_token

router = APIRouter()

@router.post("/login", tags=["auth"])
def login(user: User):
    if user.email == "admin" and user.password == "admin":
        token = create_token(vars(user))
        return JSONResponse(status_code=200, content={"token": token})
    return JSONResponse(status_code=401, content={"message": "Unauthorized"})