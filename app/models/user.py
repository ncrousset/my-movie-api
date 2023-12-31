from config.database import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship
from app.models.relationship import user_favorite_movies

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(25), nullable=False)
    created_at = Column(DateTime(True), default=datetime.now())
    active = Column(Boolean, default=True)
    
    movies_favorite = relationship("Movie", secondary=user_favorite_movies,
                                      back_populates="users_favorite")

    def __str__(self):
        return f"{self.id} - {self.email} - {self.password}"