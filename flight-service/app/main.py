from fastapi import FastAPI
from app.api.routes import flight

app = FastAPI()

app.include_router(flight.router, prefix="/flight")

