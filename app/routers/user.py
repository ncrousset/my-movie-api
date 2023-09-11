from fastapi import APIRouter, Path, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from config.database import Session
from app.services.user import UserService  
from app.schemas.user import User
from app.utils.jwt_manager import create_token
from app.middlewares.jwt_bearer import JWTBearer
from app.utils.serializer import custom_serializer


router = APIRouter()

@router.get("/user/{user_id}", tags=["user"],  status_code=200, response_model=User, dependencies=[Depends(JWTBearer())])
def get_user(user_id: int = Path(ge=1)) -> User:
    db = Session()
    result = UserService(db).get_user_by_id(user_id)

    if not result:
        return JSONResponse(status_code=404, content={"message": "User not found"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@router.post("/user", tags=["user"])
def register_user(user: User):
    db = Session()
    result = UserService(db).register_user(user)

    if not result:
        return JSONResponse(status_code=400, content={"message": "User already exists"})

    user.created_at = custom_serializer(user.created_at)

    token = create_token(vars(user))

    return JSONResponse(status_code=201, content={"token": token})