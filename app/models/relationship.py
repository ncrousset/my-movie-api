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
