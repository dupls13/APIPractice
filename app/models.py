from sqlalchemy import Column, Integer, String
from .database import Base 

#Create class for Users, extend to base 
class User(Base):
    __tablename__ = 'users'
    # Columns 
    user_id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable = False)
    username = Column(String, nullable=False)
    password = Column(String, nullable= False)

