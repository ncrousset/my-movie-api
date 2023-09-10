import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session  import sessionmaker
from sqlalchemy.orm import DeclarativeBase

enviroment = os.getenv("APP_ENV", "production")

if enviroment == "testing":
    sqlite_file_name = "../database_test.sqlite"
else:
    sqlite_file_name = "../database.sqlite"

base_dir = os.path.dirname(os.path.realpath(__file__))
database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"
engine = create_engine(database_url, echo=True)

Session = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass
