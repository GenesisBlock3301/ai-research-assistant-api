from fastapi import FastAPI
from app.api.v1 import user_router, chat_router, document_router
from app.middlewares import AuthMiddleware

app = FastAPI(title="Personal Research Agent")

app.add_middleware(AuthMiddleware)
app.include_router(user_router, prefix="/api/v1/users", tags=["users"])
app.include_router(chat_router, prefix="/api/v1/chats", tags=["chats"])
app.include_router(document_router, prefix="/api/v1/documents", tags=["documents"])
