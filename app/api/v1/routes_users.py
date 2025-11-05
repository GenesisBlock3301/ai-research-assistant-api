from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from jose import jwt

from app.config import settings
from app.db.base import get_db
from app.db.models import User
from app.schemas.user import UserCreate, UserRead, TokenResponse
from app.utils import get_current_user

user_router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@user_router.post("/register", response_model=UserRead)
def register(user: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed = pwd_context.hash(user.password)
    db_user = User(email=user.email, hashed_password=hashed)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@user_router.post("/login", response_model=TokenResponse)
def login(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not pwd_context.verify(user.password, db_user.hashed_password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")
    token = jwt.encode({"sub": str(db_user.id)}, settings.SECRET_KEY, algorithm="HS256")
    return {"access_token": token, "token_type": "bearer", "user": db_user}

@user_router.get("/me", response_model=UserRead)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user