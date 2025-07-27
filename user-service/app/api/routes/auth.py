from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.db.schemas.user import UserCreate, Token
from app.db.session import get_db
from app.db.models.user import User
from app.core.security import hash_password, verify_password, create_access_token
from app.services.auth_service import register_user, authenticate_user
router = APIRouter()

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(user: UserCreate, db: Session = Depends(get_db)):
    
    db_user = register_user(user, db)

    return {"message": "User created successfully", "user_id": db_user.id}


@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    access_token, user = authenticate_user(form_data.username, form_data.password, db)
    return {"access_token": access_token, "token_type": "bearer"}
