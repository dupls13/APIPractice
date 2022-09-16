from pydantic import BaseModel, EmailStr

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
    

