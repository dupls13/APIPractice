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
from .routers import users



app = FastAPI()

#Connect model 
models.Base.metadata.create_all(bind=engine)

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


# Connnect routers 
app.include_router(users.router)

@app.get('/')
def root():
    return {'message': "Welcome"} 


#           Post