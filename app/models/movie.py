from config.database import Base
from sqlalchemy import Column, Integer, String, Float

from pydantic import BaseModel, Field

class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    year = Column(Integer, nullable=False)
    category = Column(String(100), nullable=False)
    rating = Column(Float, nullable=False)

    def __str__(self):
        return f"{self.id} - {self.name} - {self.year} - {self.category} - {self.rating}"

class MovieA(BaseModel):
    id: int
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