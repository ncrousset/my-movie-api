from typing import Optional, List
from pydantic import BaseModel, Field
from app.schemas.category import Category


class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=1, max_length=100)
    summary: Optional[str] = Field(None ,min_length=1, max_length=500)
    director: Optional[str] = Field(None, min_length=1, max_length=200)
    year: int = Field(ge=1900, le=2021)
    imdb_rating: Optional[float] = Field(None, ge=0.1, le=10)
    image_url: Optional[str] = Field(None, min_length=1, max_length=500)

    categories: List[Category]

    class Config:
        json_schema_extra = {
            "example": {
                "title": "The Godfather",
                "summary": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
                "director": "Francis Ford Coppola",
                "year": 1972,
                "imdb_rating": 9.2,
                "image_url": "https://m.media-amazon.com/images/I/51NpxYy1EGL._AC_.jpg",
                "categories": [
                    {"id": 1, "name": "Action"},
                    {"id": 2, "name": "Adventure"},
                    {"id": 3, "name": "Animation"}
                ]
            }
        }