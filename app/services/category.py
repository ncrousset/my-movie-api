from app.models.movie import  Category as CategoryModel

class CategoryService():
    def __init__(self, db) -> None:
        self.db = db

    def get_category(self, id):
        result = self.db.query(CategoryModel).filter(CategoryModel.id == id).first()
        return result