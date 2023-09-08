from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer
from app.utils.jwt_manager import validate_token

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        if auth:
            if not validate_token(auth.credentials):
                raise HTTPException(status_code=403, detail="Invalid username or password")
            return auth.credentials