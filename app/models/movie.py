from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from config.database import Base
from app.models.relationship import movies_categories, user_favorite_movies


class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False, unique=True)
    summary = Column(String(500))
    director = Column(String(200))
    year = Column(Integer, nullable=False)
    imdb_rating = Column(Float)
    image_url = Column(String(500))

    categories = relationship("Category", secondary=movies_categories,
                              back_populates="movies")
    
    users_favorite = relationship("User", secondary=user_favorite_movies,
                                    back_populates="movies_favorite")

    def __repr__(self):
        return f"<Movie {self.title}>"

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)

    movies = relationship("Movie", secondary=movies_categories,
                          back_populates="categories")

    def __repr__(self):
        return f"<Category {self.name}>"