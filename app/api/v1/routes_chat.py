from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from app.api.v1.deps import get_current_user
from app.db import get_db
from app.services import LLaMAWrapper, VectorStore, EmbeddingService

chat_router = APIRouter()
embedding_service = EmbeddingService()
llm = LLaMAWrapper(endpoint="http://localhost:11434/api/generate")

# current_user=Depends(get_current_user)
@chat_router.get("/chat")
def chat(query: str, db: Session=Depends(get_db)):
    vector_store = VectorStore(db)
    q_emb = embedding_service.embed_texts([query])[0]
    results = vector_store.query(q_emb, top_k=5).all()
    context = "\n".join([r.chunk_text for r in results])
    prompt = f"Answer the question based on context:\n{context}\nQuestion: {query}"
    answer = llm._call(prompt)
    return {"answer": answer, "sources": [r.document_id for r in results]}
