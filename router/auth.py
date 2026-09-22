from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import get_db
from schemas import UserCreate, UserLogin
from models import User
from security import hash_password, verify_password, create_access_token, get_current_user


router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register")
def register(user:UserCreate, db:Session = Depends(get_db)):

    password = hash_password(user.password)

    new_user = User(
        name = user.name,
        email = user.email,
        hash_password = password
    )  

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User Register successfully",
        "user_id": new_user.id
    }

@router.post("/login")
def login(user:UserLogin, db:Session = Depends(get_db)):

    db_user = db.execute(select(User).where(User.email == user.email)).scalar_one_or_none()

    if not db_user:
        return {
            "error": "Invalid email or password"
        }

    if not verify_password(user.password, db_user.hash_password):
        return {
            "error": "Invalid email or password"
        }

    # token generate
    token = create_access_token(db_user.id)

    return {
        "message": "Login Successfull",
        "access_token": token
    }

@router.get("/me")
def profile(current_user:User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "email": current_user.email,
        "name": current_user.name
    }


    
    

