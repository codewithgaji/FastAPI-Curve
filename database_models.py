from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base() # This is used to track models 

class Product(Base):

  # Creating the DB Table Constructor
  __tablename__ = "product"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String)
  description = Column(String)
  price = Column(Float)
  quantity = Column(Integer)