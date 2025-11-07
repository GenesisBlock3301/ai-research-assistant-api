from langchain_postgres import PGVector
from langchain.chains import RetrievalQA
from langchain_community.embeddings import OllamaEmbeddings
from app.config import settings


embeddings = OllamaEmbeddings(model="nomic-embed-text")

vector_store = PGVector(
    embeddings=embeddings,
    collection_name="document_chunks_collection",
    connection=settings.DATABASE_URL,
    use_jsonb=True,
)



