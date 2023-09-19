from fastapi import HTTPException

class WithOutCategoryError(Exception):
    def __init__(self):
        self.message = "Movie must have at least one category"

class UserAlreadyExistsError(HTTPException):
    def __init__(self, email):
        detail = f"The email '{email}' is already in use."
        super().__init__(status_code=400, detail=detail)

class UserNotFoundError(HTTPException):
    def __init__(self, id):
        detail = f"The user with id '{id}' was not found."
        super().__init__(status_code=404, detail=detail)

class UserNotFoundErrorByEmail(HTTPException):
    def __init__(self, email):
        detail = f"The user with email '{email}' was not found."
        super().__init__(status_code=404, detail=detail)