from pydantic import BaseModel, Field

class User(BaseModel):
    email: str
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "password": "password",
                "email": ""
            }
        }