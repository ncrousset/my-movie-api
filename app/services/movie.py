from app.models.movie import Movie as MovieModel
from app.schemas.movie import Movie

class MovieService():

    def __init__(self, db) -> None:
        self.db = db

    def get_movies(self):
        result = self.db.query(MovieModel).all()
        return result
    
    def get_movie(self, id):
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        return result
    
    def get_movies_by_category(self, category):
        return []
        # result = self.db.query(MovieModel).filter(MovieModel.category.like(f"%{category}%")).all()
        # return result
    
    def create_movie(self, movie: Movie):
        try:
            new_movie = MovieModel(**vars(movie))
            self.db.add(new_movie)
            self.db.commit()
        except Exception as e:
            return None
        
        return new_movie
    
    def update_movie(self, id, movie: Movie):
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        if not result:
            return None
        result.title = movie.title
        result.obi = movie.obi
        result.director = movie.director
        result.year = movie.year
        result.imdb_rating = movie.imdb_rating
        result.image_url = movie.image_url
        self.db.commit()
        return result
    
    def delete_movie(self, id):
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        if not result:
            return None
        self.db.delete(result)
        self.db.commit()
        return result