from typing import Optional
from pydantic import BaseModel, Field

class Movie(BaseModel):
    id: Optional[int] = None 
    name: str = Field(..., max_length=50)
    year: int = Field(..., gt=1900, lt=2100)
    category: str = Field(..., max_length=100, min_length=3)
    rating: float = Field(...,le=10, ge=0)

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "The Godfather",
                "year": 1972,
                "category": "Crimen/Drama",
                "rating": 9.2
            }
        }

    def __str__(self):
        return f"{self.id} - {self.name} - {self.year} - {self.category} - {self.rating}"