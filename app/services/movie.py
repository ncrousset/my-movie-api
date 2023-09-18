from app.models.movie import Movie as MovieModel, Category as CategoryModel
from app.schemas.movie import Movie
from app.utils.error import WithOutCategoryError
from app.services.category import CategoryService

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
        """
        Get a list of movies by category.
        :param category: La categoría de las películas que se desean obtener.
        :type category: strs
        :return: Una lista de películas que pertenecen a la categoría especificada.
        """
        result = (self.db.query(MovieModel)
                         .filter(MovieModel.categories.any(CategoryModel.name == category))
                         .all())

        return result

    def create_movie(self, movie: Movie):
        try:
            categories = movie.categories
            del movie.categories

            # Add categories to movie
            if len(categories) > 0:
                categories = [CategoryService(self.db).get_category(category.id)
                              for category in categories]
            else:
                raise WithOutCategoryError()

            new_movie = MovieModel(**vars(movie))
            new_movie.categories = categories
            self.db.add(new_movie)
            self.db.commit()
        except Exception as e:
            raise Exception(e)

        return new_movie


    def update_movie(self, id, movie: Movie):
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        if not result:
            return None
        result.title = movie.title
        result.summary = movie.summary
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