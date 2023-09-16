from config.database import Session
from app.models.user import User
from app.models.movie import Category, Movie


categories_movies = [
    Category(name="Action"),
    Category(name="Adventure"),
    Category(name="Animation"),
    Category(name="Biography"),
    Category(name="Comedy"),
    Category(name="Crime"),
    Category(name="Documentary"),
    Category(name="Drama"),
    Category(name="Family"),
    Category(name="Fantasy"),
    Category(name="Film Noir"),
    Category(name="History"),
    Category(name="Horror"),
    Category(name="Music"),
    Category(name="Musical"),
    Category(name="Mystery"),
    Category(name="Romance"),
    Category(name="Sci-Fi"),
    Category(name="Short Film"),
    Category(name="Sport"),
    Category(name="Superhero"),
    Category(name="Thriller"),
    Category(name="War"),
    Category(name="Western")
]

user = User(name="admin", email="test@gmail.com", password="123456")

session = Session()
session.add_all(categories_movies + [user])
session.commit()