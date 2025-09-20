from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from app.api.v1.deps import get_current_user
from app.db import get_db, User
from app.services import LLaMAWrapper, VectorStore, EmbeddingService, get_retrieval_qa
from app.services.langgraph_nodes import multiline_step_qa

chat_router = APIRouter()
embedding_service = EmbeddingService()
llm = LLaMAWrapper(endpoint="http://localhost:11434/api/generate")

# current_user=Depends(get_current_user)
# Manually
# @chat_router.get("/chat")
# def chat(query: str, db: Session=Depends(get_db)):
#     vector_store = VectorStore(db)
#     q_emb = embedding_service.embed_texts([query])[0]
#     results = vector_store.query(q_emb, top_k=5).all()
#     context = "\n".join([r.chunk_text for r in results])
#     prompt = f"Answer the question based on context:\n{context}\nQuestion: {query}"
#     answer = llm._call(prompt)
#     return {"answer": answer, "sources": [r.document_id for r in results]}

qa = get_retrieval_qa()


@chat_router.get("/chat")
def chat(query: str):
    """single-step RetrievalQA (good for quick Q&A)."""
    result = qa.invoke(query)
    return {"answer": result['result'], "sources": [d.metadata for d in result['source_documents']]}


@chat_router.post("/chat/multiline")
def chat_multiline(query: str):
    result = multiline_step_qa(query)
    return {
        "summary": result['summary'],
        "sources": [d.metadata for d in result["docs"]],
    }
