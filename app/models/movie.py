from config.database import Base
from sqlalchemy import Column, Integer, String, Float

class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    year = Column(Integer, nullable=False)
    category = Column(String(100), nullable=False)
    rating = Column(Float, nullable=False)

    def __str__(self):
        return f"{self.id} - {self.name} - {self.year} - {self.category} - {self.rating}"