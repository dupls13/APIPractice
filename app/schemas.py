from pydantic import BaseModel, EmailStr
from datetime import datetime 

# User information 
class User(BaseModel): 
    email: EmailStr
    username: str 
    password: str

class UserCreate(User):
    pass 

# Output when requesting User
class UserOut(BaseModel): 
    user_id: int 
    email: EmailStr
    username: str
    
    class Config: 
        orm_mode = True 
    



# Post information 

class Post(BaseModel): 
    title: str
    content: str 
    
class PostCreate(Post): 
    pass


class PostOut(Post):
    time: datetime

    class Config: 
        orm_mode = True 