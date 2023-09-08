from sqlalchemy import Column, Integer, String, Float
from config.database import Base

class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    obi = Column(String(500))
    category = Column(String(200))
    director = Column(String(200))
    year = Column(Integer, nullable=False)
    imdb_rating = Column(Float)
    image_url = Column(String(500))