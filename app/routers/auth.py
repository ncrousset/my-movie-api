from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.schemas.user import User
from app.utils.jwt_manager import create_token
from app.services.user import UserService
from config.database import Session
from fastapi.encoders import jsonable_encoder
from app.utils.error import UserNotFoundErrorByEmail
from app.models.user import User as UserModel

router = APIRouter()

@router.post("/login", tags=["auth"])
def login(user: User.Auth):
    db = Session()

    try:
        db_user = UserService(db).get_user_by_email(user.email)
    except UserNotFoundErrorByEmail as e:
        return JSONResponse(status_code=e.status_code, content={"message": e.detail})
    except Exception as e:
        return JSONResponse(status_code=404, content={"message": str(e)})   

    if db_user.password == user.password:
        token = create_token(vars(user))
        return JSONResponse(status_code=200, content={"token": token})
    return JSONResponse(status_code=401, content={"message": "Unauthorized"})