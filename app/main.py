from fastapi import FastAPI
from app.api.v1 import user_router

app = FastAPI(title="Personal Research Agent")

app.include_router(user_router, prefix="/api/v1/users", tags=["users"])
