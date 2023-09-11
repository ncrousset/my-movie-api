from app.models.user import User as UserModel

class UserService():
    def __init__(self, db) -> None:
        self.db = db

    def get_users(self):
        result = self.db.query(UserModel).all()
        return result

    def get_user_by_id(self, id):
        result = self.db.query(UserModel).filter(UserModel.id == id).first()
        return result
    
    def get_user_by_email(self, email):
        result = self.db.query(UserModel).filter(UserModel.email == email).first()
        return result
    
    def register_user(self, user):
        result = self.get_user_by_email(user.email)
        if result:
            return None

        try:
            new_user = UserModel(**vars(user))
            self.db.add(new_user)
            # self.db.commit()
        except Exception as e:
            return e

        return new_user

    def update_user(self, id, user):
        result = self.db.query(UserModel).filter(UserModel.id == id).first()
        if not result:
            return None
        result.email = user.email
        result.password = user.password
        self.db.commit()
        return result