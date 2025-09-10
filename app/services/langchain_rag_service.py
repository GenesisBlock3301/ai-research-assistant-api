from langchain_community.vectorstores import PGVector
from langchain.chains import RetrievalQA
from langchain_community.embeddings import SentenceTransformerEmbeddings
from app.config import settings
from app.services.llama_service import LLaMAWrapper


def get_retrieval_qa():
    """
    Create a RetrievalQA chain using PostgreSQL vector store and LLaMA LLM.

    Returns:
        RetrievalQA instance ready to perform RAG (Retrieval-Augmented Generation) queries.
    """

    # 1️⃣ Initialize embeddings
    embeddings = SentenceTransformerEmbeddings(model_name=settings.EMBEDDING_MODEL_NAME)

    # 2️⃣ Initialize vector store (PGVector) with JSONB metadata
    vectorstore = PGVector(
        connection_string=settings.DATABASE_URL,
        embedding_function=embeddings,
        collection_name="document_chunks"  # ✅ Use JSONB for faster filtering
    )

    # 3️⃣ Create retriever
    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 5}
    )

    # 4️⃣ Initialize LLaMA LLM wrapper
    llm = LLaMAWrapper(endpoint=settings.LLM_SERVER_URL)

    # 5️⃣ Create RetrievalQA chain
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",  # Combines retrieved docs into a single prompt
        return_source_documents=True  # Include document sources in the output
    )

    return qa
