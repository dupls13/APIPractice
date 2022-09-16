from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text 
from .database import Base 


#Create class for Users, extend to base 
class User(Base):
    __tablename__ = 'users'
    # Columns 
    user_id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable = False)
    username = Column(String, nullable=False)
    password = Column(String, nullable= False)

class Post(Base): 
    __tablename__ = 'posts'
    post_id = Column(Integer, primary_key = True, nullable = False)
    title = Column(String, nullable = False)
    content = Column(String, nullable = False)
    time = Column(TIMESTAMP(timezone=True), nullable= False, server_default = text('now()'))