from sqlalchemy import Table, Column, Integer, ForeignKey
from config.database import Base


movies_categories = Table(
        'movies_has_categories',
        Base.metadata,
        Column('movie_id', Integer,
               ForeignKey('movies.id'), primary_key=True),
        Column('category_id', Integer,
               ForeignKey('categories.id'), primary_key=True)
    )


user_favorite_movies = Table(
        'users_has_movies',
        Base.metadata,
        Column('user_id', Integer,
                 ForeignKey('users.id'), primary_key=True),
        Column('movie_id', Integer,
                ForeignKey('movies.id'), primary_key=True)
        )