from fastapi import APIRouter, Depends
from app.dependencies.auth import get_current_user
from app.db.models.user import User

router = APIRouter()

@router.get("/me")
def read_me(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email,
        "role": current_user.role
    }