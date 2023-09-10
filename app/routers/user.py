from fastapi import APIRouter, Path, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from config.database import Session
from app.services.user import UserService  
from app.schemas.user import User
from app.utils.jwt_manager import create_token
from email_validator import validate_email, EmailNotValidError
from app.middlewares.jwt_bearer import JWTBearer


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
    if validate_email(user.email) == False:
        return JSONResponse(status_code=400, content={"message": "Invalid email"})

    db = Session()
    result = UserService(db).register_user(user)
    if not result:
        return JSONResponse(status_code=400, content={"message": "User already exists"})
    
    token = create_token(vars(user))
    return JSONResponse(status_code=201, content={"token": token})