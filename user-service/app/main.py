from fastapi import FastAPI
from app.api.routes import auth, users

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/user")
