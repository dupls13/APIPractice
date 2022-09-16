from multiprocessing import synchronize
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session 
from typing import List 

from ..database import get_db
from .. import schemas, models

# Create router
router = APIRouter(
    prefix='/posts', 
    tags=['Posts']
)


# Get all posts 
@router.get('/', response_model=List[schemas.PostOut])
def get_post(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts 


# Create new post 
@router.post('/', response_model=schemas.PostOut)
def create_post(new_post:schemas.PostCreate, db: Session = Depends(get_db)):
    new = models.Post(**new_post.dict())
    db.add(new)
    db.commit()
    db.refresh(new)
    
    return new 


#Get specific post 
@router.get('/{post_id}', response_model = schemas.PostOut)
def get_postid(post_id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.post_id == post_id).first()
    
    return post 

# Delete specific post 
@router.delete('/{post_id}')
def delete_post(post_id: int, db:Session = Depends(get_db)): 
    post = db.query(models.Post).filter(models.Post.post_id == post_id).first()
    
    post.delete(synchronize_session = False)
    db.commit()
    
    return post 

# Update specific post 
@router.put('/{post_id}', response_model = schemas.PostOut)
def update_post(post_id: int, updated_post:schemas.PostCreate, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.post_id == post_id).first()
    
    post.update(updated_post.dict(), synchronize_session = False)
    db.commit()
    
    return post.first()
    
