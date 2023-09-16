from typing import Optional
from pydantic import BaseModel, Field

class Category(BaseModel):
    id: Optional[int] = None
    name: str = Field(min_length=1, max_length=50)

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Action"
            }
        }