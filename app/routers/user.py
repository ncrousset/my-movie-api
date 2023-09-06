from fastapi import APIRouter, Path
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from config.database import Session
from app.services.user import UserService  
from app.schemas.user import User
from app.utils.jwt_manager import create_token


router = APIRouter()

@router.get("/user/{user_id}", tags=["user"])
def get_user(user_id: int = Path(ge=1)) -> User:
    db = Session()
    result = UserService(db).get_user_by_id(user_id)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@router.post("/user", tags=["user"])
def register_user(user: User):
    db = Session()
    result = UserService(db).register_user(user)
    if not result:
        return JSONResponse(status_code=400, content={"message": "User already exists"})
    
    token = create_token(vars(user))
    return JSONResponse(status_code=201, content={"token": token})