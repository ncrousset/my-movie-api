from app.models.user import User as UserModel
from app.utils.error import UserAlreadyExistsError, \
                            UserNotFoundError, UserNotFoundErrorByEmail

class UserService():
    def __init__(self, db) -> None:
        self.db = db

    def get_users(self):
        result = self.db.query(UserModel).all()
        return result

    def get_user_by_id(self, id):
        result = self.db.query(UserModel).filter(UserModel.id == id).first()
        if not result:
            raise UserNotFoundError(id)

        return result
    
    def get_user_by_email(self, email):
        result = self.db.query(UserModel).filter(UserModel.email == email).first()
        if not result:
            raise UserNotFoundErrorByEmail(email)

        return result
    
    def register_user(self, user):
        result = self.db.query(UserModel)\
                        .filter(UserModel.email == user.email).first()

        if result:
            raise UserAlreadyExistsError(user.email)

        try:
            new_user = UserModel(**vars(user))
            self.db.add(new_user)
            self.db.commit()
        except Exception as e:
            return e

        return new_user

    def update_user(self, id, user):
        result = self.db.query(UserModel).filter(UserModel.id == id).first()
        
        if not result:
            return UserNotFoundError(id)

        result.email = user.email
        result.password = user.password
        self.db.commit()
        return result
    
    def desactivate_user(self, id):
        result = self.db.query(UserModel).filter(UserModel.id == id).first()
        
        if not result:
            return UserNotFoundError(id)

        result.active = False
        self.db.commit()
        return result
    
    def activate_user(self, id):
        result = self.db.query(UserModel).filter(UserModel.id == id).first()
        
        if not result:
            return UserNotFoundError(id)

        result.active = True
        self.db.commit()
        return result