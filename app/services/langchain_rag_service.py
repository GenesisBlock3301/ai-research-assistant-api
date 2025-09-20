from langchain_postgres import PGVector
from langchain.chains import RetrievalQA
from langchain_huggingface import HuggingFaceEmbeddings
from app.config import settings
from app.services.llama_service import LLaMAWrapper


def get_retrieval_qa() -> RetrievalQA:

    # Initialize embeddings
    embeddings = HuggingFaceEmbeddings(model_name=settings.EMBEDDING_MODEL_NAME)

    # Initialize PGVector vector store (new API)

    vector_store = PGVector(
        embeddings=embeddings,
        collection_name="document_chunks_collection",
        connection=settings.DATABASE_URL,
        use_jsonb=True,
    )

    # Create retriever
    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 5}
    )

    # Initialize LLaMA LLM wrapper
    llm = LLaMAWrapper(endpoint=settings.LLM_SERVER_URL)

    # Create RetrievalQA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        return_source_documents=True
    )

    return qa_chain
