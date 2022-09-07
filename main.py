from fastapi import FastAPI, Response 
from pydantic import BaseModel 
from random import randrange


app = FastAPI()


user_data= [{"username": "shawdt" , "password": "1234"}]

post_data=[{"username": "shawdt", "title": "Test post 1", "post_number": 1, "content": "This is my first post"}]

# User information 
class UserModel(BaseModel): 
    username = str 
    password = str
    
# Post information 
class Post(BaseModel):
    username = UserModel.username
    title = str
    post_number = int 
    content: str 
    id: int 
    


# Functions 

def find_username(username, password): 
    for username in user_data: 
        if username['username'] == username:
            for password in user_data: 
                if password['password'] == password:
                    return UserModel 
        
    


# Homepage 
@app.get("/")
def root():
    return {"Homepage"}

# Login Page
@app.get("/login")
def login_user(username: str, password: str, response: Response):
    return 


@app.get('/users')
def get_user(user : UserModel):
    return {"data": user_data}
    
# Individual User Page Creation
@app.put('/user')
def create_user(user: UserModel):
    return {"data": user_data}


# See posts page
@app.get('/posts')
def get_post():
    return {"data": post_data}


# Create Posts Page 
@app.post('/posts/create')
def create_post(post: Post): 
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 100000)
    post_data.append(post_dict)
    return {"data": post_dict}
    