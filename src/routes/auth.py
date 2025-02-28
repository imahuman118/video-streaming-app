from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.user import UserCreate, UserUpdate, UserResponse
from models.user import User
from config.database import get_db
from middleware.auth import verify_token

router = APIRouter()

@router.post("/users", response_model=UserResponse)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Check if user already exists
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Create new user
    hashed_password = User.hash_password(user.password)
    db_user = User(email=user.email, password=hashed_password)
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user

@router.put("/users/me", response_model=UserResponse)
async def update_user(
    user_update: UserUpdate,
    token_data: dict = Depends(verify_token),
    db: Session = Depends(get_db)
):
    # Get current user
    current_user = db.query(User).filter(User.id == token_data["user_id"]).first()
    if not current_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Update user fields
    if user_update.email:
        # Check if email is already taken by another user
        existing_user = db.query(User).filter(
            User.email == user_update.email,
            User.id != current_user.id
        ).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        current_user.email = user_update.email
    
    if user_update.password:
        current_user.password = User.hash_password(user_update.password)
    
    db.commit()
    db.refresh(current_user)
    
    return current_user 