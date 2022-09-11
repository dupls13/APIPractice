from sqlalchemy import Column, Integer, String
from .database import Base 

#Create class for Users, extend to base 
class User(Base):
    __tablename__ = 'users'
    # Columns 
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, nullable=False)
    pw = Column(String, nullable= False)

