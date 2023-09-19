from fastapi import APIRouter, Path, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from config.database import Session
from app.services.user import UserService  
from app.schemas.user import User
from app.utils.jwt_manager import create_token
from app.middlewares.jwt_bearer import JWTBearer
from app.utils.serializer import custom_serializer
from app.utils.error import UserNotFoundError, UserAlreadyExistsError


router = APIRouter()

@router.get("/user/{user_id}", tags=["user"],  status_code=200, response_model=User, dependencies=[Depends(JWTBearer())])
def get_user(user_id: int = Path(ge=1)) -> User:
    db = Session()
    try:
        result = UserService(db).get_user_by_id(user_id)
    except UserNotFoundError as e:
        return JSONResponse(status_code=e.status_code, content={"message": e.detail})
    except Exception as e:
        return JSONResponse(status_code=404, content={"message": str(e)})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@router.post("/user", tags=["user"])
def register_user(user: User):
    db = Session()

    try:
        register_user = UserService(db).register_user(user)
        user.created_at = custom_serializer(register_user.created_at)
        token = create_token(vars(register_user))
    except UserAlreadyExistsError as e:
        return JSONResponse(status_code=e.status_code, content={"message": e.detail}) 
    except Exception as e:
        return JSONResponse(status_code=404, content={"message": str(e)})

    return JSONResponse(status_code=201, content={"token": token})