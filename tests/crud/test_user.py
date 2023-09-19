import tests.test_main
from config.database import Session
from app.services.user import UserService
from app.schemas.user import User
from app.utils.error import UserAlreadyExistsError, UserNotFoundError, UserNotFoundErrorByEmail
from faker import Faker


db = Session()
faker = Faker()


user_data = User(
        email=faker.email(),
        password="passwordaa",
        name=faker.name(),
    )

def test_register_user():
    try:
        user =  UserService(db).register_user(user_data)
    except Exception as e:
        print(e)

    assert user.email == user_data.email

def test_register_user_already_exists():
    try:
        UserService(db).register_user(user_data)
    except Exception as e:
        assert isinstance(e, UserAlreadyExistsError)


def test_get_users():
    users = UserService(db).get_users()
    assert len(users) > 0

def test_get_user_by_id():
    user = UserService(db).get_user_by_id(1)
    assert user.id == 1

def test_get_user_by_id_not_found():
    try:
        UserService(db).get_user_by_id(100)
    except Exception as e:
        assert isinstance(e, UserNotFoundError)
    
def test_get_user_by_email():
    user = UserService(db).get_user_by_email(user_data.email)
    assert user.email == user_data.email

def test_get_user_by_email_not_found():
    try:
        UserService(db).get_user_by_email("lolo@gmail.com")
    except Exception as e:
        assert isinstance(e, UserNotFoundErrorByEmail)

def test_update_user():
    user_data.email = "update@gmail.com"
    try:
        user = UserService(db).update_user(1, user_data)
    except Exception as e:
        print(e)

    assert user.email == user_data.email

def test_update_user_not_found():
    try:
        UserService(db).update_user(100, user_data)
    except Exception as e:
        assert isinstance(e, UserNotFoundError)

def test_desactivate_user():
    try:
        user = UserService(db).desactivate_user(1)
    except Exception as e:
        print(e)

    assert user.active == False

def test_desactivate_user_not_found():
    try:
        UserService(db).desactivate_user(100)
    except Exception as e:
        assert isinstance(e, UserNotFoundError)

def test_activate_user():
    try:
        user = UserService(db).activate_user(1)
    except Exception as e:
        print(e)

    assert user.active == True

def test_activate_user_not_found():
    try:
        UserService(db).activate_user(100)
    except Exception as e:
        assert isinstance(e, UserNotFoundError)