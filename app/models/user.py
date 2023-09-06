from config.database import Base
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), nullable=False)
    password = Column(String(25), nullable=False)

    def __str__(self):
        return f"{self.id} - {self.email} - {self.password}"