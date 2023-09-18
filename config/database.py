import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm import DeclarativeBase
from dotenv import load_dotenv

load_dotenv()

enviroment = os.environ.get("APP_ENV")

DB_NAME = os.environ.get("DB_NAME")
DB_USER_NAME = os.environ.get("DB_USER_NAME")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_HOST = os.environ.get("DB_HOST")

if enviroment == "testing":
    sqlite_file_name = "../database_test.sqlite"
    base_dir = os.path.dirname(os.path.realpath(__file__))

    # Remove sqlite file if exists before create a new one
    if not os.path.exists(sqlite_file_name):
        os.remove(os.path.join(base_dir, sqlite_file_name))

    database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"
else:
    database_url = f"mysql+mysqlconnector://{DB_USER_NAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

engine = create_engine(database_url, echo=True)

Session = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass
