from fastapi import FastAPI
from app.api.routes import booking

app = FastAPI()

app.include_router(booking.router, prefix="/booking")

