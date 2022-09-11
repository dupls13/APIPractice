from fastapi import FastAPI, Response , status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel 
from typing import Optional 
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
from sqlalchemy.orm import Session 
from . import models 
from .database import engine, get_db



app = FastAPI()

#Connect model 
models.Base.metadata.create_all(bind=engine)


user_data= [{"username": "shawdt" , "pw": "1234"}]

post_data=[{"username": "shawdt", "title": "Test post 1", "post_number": 1, "content": "This is my first post"}]

# User information 
class User(BaseModel): 
    username = str 
    pw = str
    id = int
    
# Post information 
class Post(BaseModel):
    username = User.username
    title = str
    post_number = int 
    content: str 
    post_id: int 
    

# Connect to database 
while True:
    try: 
        conn = psycopg2.connect(host='localhost', database='mockapi', 
                                user='postgres', password='3875', 
                                cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successful")
        break 
    except Exception as error: 
        print("Connecting to database failed")
        print("Error: ", error)




# Functions 

def find_username(username, paswword): 
    for username in user_data: 
        if username['username'] == username:
            for password in user_data: 
                if password['password'] == password:
                    return User 
        

@app.get('/')
def root():
    return {'message': "Welcome"} 


#           Users

#Get user data
@app.get('/users')
def get_user(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return {'data': users}

# Create user 
@app.post('/users', status_code=status.HTTP_201_CREATED)
def create_user(user:User, db: Session = Depends(get_db)):
    
    cursor.execute("""INSERT INTO users (username, pw) VALUES (%s, %s) RETURNING * """,
                   (user.username, user.pw))
    new_user = cursor.fetchone()
    conn.commit()
    #new_user = models.User(**user.dict())

    #db.add(new_user)
    #db.commit()
    #db.refresh(new_user)
    return {"data": new_user}


#Edit user 
@app.put('/user/{user_id}')
def update_user(user_id: int, user: User):
    
    
    print(User)
    return {'data': user}

# Delete User
@app.delete('/user/{user_id}')
def delete_user(user_id: int):
    return {'user': user_data}






#           Post