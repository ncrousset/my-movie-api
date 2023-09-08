from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.schemas.user import User
from app.utils.jwt_manager import create_token
from app.services.user import UserService
from config.database import Session
import uvicorn

router = APIRouter()

@router.post("/login", tags=["auth"])
def login(user: User):
    db = Session()
    db_user = UserService(db).get_user_by_email(user.email)
    if not db_user:
        return JSONResponse(status_code=404, content={"message": "User not found"})

    if  db_user.password == user.password:
        token = create_token(vars(user))
        return JSONResponse(status_code=200, content={"token": token})
    return JSONResponse(status_code=401, content={"message": "Unauthorized"})