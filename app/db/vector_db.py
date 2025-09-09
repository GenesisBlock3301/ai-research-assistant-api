from langchain.vectorstores import PGVector
from langchain.embeddings import SentenceTransformerEmbeddings
from sqlalchemy import create_engine
from app.config import settings

# Create embedding objects
embeddings = SentenceTransformerEmbeddings(model_name=settings.vector_model_name)


# Connect to Postgres
engine = create_engine(settings.DATABASE_URL)

vectorstore = PGVector(
    connection_string=settings.DATABASE_URL,
    embeddings=embeddings,
    collection_name="document_chunks",
)


texts = [
    "This is a sample chunk from a CV paper about object detection.",
    "Another chunk about GANs for image synthesis."
]

vectorstore.add_texts(texts)


