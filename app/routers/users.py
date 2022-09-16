from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session 
from typing import List

from ..database import get_db 
from .. import models, schemas

router = APIRouter(
    prefix='/users', 
    tags=['Users']
)

#           Users

#Get all Users
@router.get('/', response_model= List[schemas.UserOut])
def get_user(db: Session = Depends(get_db)):
    # Grab query 
    users = db.query(models.User).all()
    return users



# Create a new User
@router.post('/', status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    
    # Collect information given, compare to User model 
    new_user = models.User(**user.dict())

    # Add new user to database 
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user



# Get Specific User based on user_id
@router.get('/{user_id}', response_model=schemas.UserOut)
def get_user(user_id: int, db:Session = Depends(get_db)):
    
    # Look for user_id in database
    user = db.query(models.User).filter(models.User.user_id == user_id).first()
  
    # If no User with no user_id found, give error
    if not user: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with id {user_id} not found')
    
    return user 


#Edit specific user based on user_id
@router.put('/{user_id}')
def update_user(user_id: int, db: Session = Depends(get_db)):
    
    # Find user with user_id 
    user_id = db.query(models.User).filter(models.user.id == id).first()
    
    # If no user_id found 
    if not user_id: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with id {user_id} not found')
    
    # Update database
    user_id.update()
    return user_id



# Delete User based on user_id 
@router.delete('/{user_id}')
def delete_user(user_id: int, db: Session = Depends(get_db)):
    
    # Find user with user_id
    user_id = db.query(models.User).filter(models.User.id == user_id)
    
    # If no user_id found, give error
    if user_id.first() == None: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with id {user_id} not found')
   
    # Update database 
    user_id.delete(sychronize_session=False)
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)