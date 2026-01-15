from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url = "postgresql://postgres:Universal1234@localhost:5432/telusko_tested" # This is the url to connnect to the db

engine = create_engine(db_url) # This is the sqlalchemy engine that binds the db to the project

session = sessionmaker(autoflush=False, autocommit=False, bind=engine) # This creates sessions and tracks the modifications to the db.