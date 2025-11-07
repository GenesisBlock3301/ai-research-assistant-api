from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session
from app.db import get_db, User
from app.services import LLaMAWrapper, EmbeddingService, get_retrieval_qa
from app.services.qa.multi_step_qa import multiline_step_qa
from app.utils import get_current_user

chat_router = APIRouter()
embedding_service = EmbeddingService()
llm = LLaMAWrapper(endpoint="http://localhost:11434/api/generate")

qa = get_retrieval_qa()


@chat_router.get("/chat")
def chat(query: str):
    try:
        result = qa.invoke(query)
        return {"answer": result['result'], "sources": [d.metadata for d in result['source_documents']]}
    except Exception as e:
        return {"error": str(e)}


@chat_router.post("/chat/multiline")
def chat_multiline(query: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    try:
        owner_id = current_user.id
        result = multiline_step_qa(query, db, owner_id)
        return {
            "summary": result['summary'],
            "sources": [d.metadata for d in result["docs"]],
        }
    except Exception as e:
        return {"error": str(e)}
