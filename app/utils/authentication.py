from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer
from app.utils.jwt_manager import validate_token

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data['email'] != "admin@email.com" and data['password'] != "admin":
            raise HTTPException(status_code=403, detail="Invalid username or password")    