from sqlalchemy import Column, Integer, String, Boolean 
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text 
from .database import Base 

#Create class for Users, extend to base 
class User(Base):
    __tablename__ = 'users'
    # Columns 
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable= False)

