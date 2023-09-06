from app.models.movie import Movie as MovieModel

class MovieService():
    def __init__(self, db) -> None:
        self.db = db

    def get_movies(self):
        result = self.db.query(MovieModel).all()
        return result

    def get_movie_by_id(self, id):
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        return result

    def get_movies_by_category(self, category):
        result = self.db.query(MovieModel).filter(MovieModel.category.like(f"%{category}%")).all()
        return result
    
    def get_movies_by_year(self, year):
        result = self.db.query(MovieModel).filter(MovieModel.year == year).all()
        return result

    def create_movie(self, movie):
        new_movie = MovieModel(**vars(movie))
        self.db.add(new_movie)
        self.db.commit()
        return new_movie

    def update_movie(self, id, movie):
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        if not result:
            return None
        result.name = movie.name
        result.year = movie.year
        result.category = movie.category
        result.rating = movie.rating
        self.db.commit()
        return result
        

    def delete(self, id):
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        if not result:
            return None
        self.db.delete(result)
        self.db.commit()
        return result