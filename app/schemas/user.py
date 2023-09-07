from pydantic import BaseModel

class User(BaseModel):
    email: str
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "password": "password",
                "email": "ncrousset926@gmail.com"
            }
        }