import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session  import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

sqlite_file_name = "../database.sqlite"
sqlite_file_name_test = "../database_test.sqlite"
base_dir = os.path.dirname(os.path.realpath(__file__)) 

database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"
database_url_test = f"sqlite:///{os.path.join(base_dir, sqlite_file_name_test)}"

engine = create_engine(database_url, echo=True)
engine_test = create_engine(database_url_test, echo=True)

Session = sessionmaker(bind=engine)
Session_test = sessionmaker(bind=engine_test)

Base = declarative_base()