from pydantic import BaseModel, EmailStr
from datetime import datetime

class User(BaseModel):
    name: str
    email: EmailStr
    password: str
    created_at: datetime = datetime.now()
    active: bool = True

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Nicolas Crousset",
                "password": "password",
                "email": "ncrousset926@gmail.com",
                "created_at": "2021-08-22T20:00:00",
                "active": True
            }
        }

    class Auth(BaseModel):
        email: EmailStr
        password: str

        class Config:
            json_schema_extra = {
                "example": {
                    "password": "password",
                    "email": "ncrousset926@gmail.com",
                }
            }