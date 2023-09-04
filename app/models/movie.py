from pydantic import BaseModel, Field

class Movie(BaseModel):
    id: int
    name: str = Field(..., max_length=50)
    year: int = Field(..., gt=1900, lt=2100)
    rating: float = Field(...,le=10, ge=0)

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "The Godfather",
                "year": 1972,
                "rating": 9.2
            }
        }

    def __str__(self):
        return f"{self.id} - {self.name} - {self.year} - {self.rating}"