from fastapi import FastAPI
from app.routers import root

app = FastAPI(title="User Service")
app.include_router(root.router)

#checking commit is okay or not