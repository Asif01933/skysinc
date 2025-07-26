from fastapi import Depends, HTTPException
from app.dependencies.auth import get_current_user
from app.db.models.user import User


def require_role(*roles: str):
    def role_checker(current_user: User = Depends(get_current_user)) -> User:
        if current_user.role not in roles:
            raise HTTPException(status_code=403, detail= "You are not authorized")
        return current_user
    return role_checker
    