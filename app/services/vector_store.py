from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import text

from app.db.models import DocumentChunk


class VectorStore:
    def __init__(self, db: Session):
        self.db = db

    def insert_chunk(self, **kwargs):
        document_id: int = kwargs.pop('document_id')
        chunk_text: str = kwargs.pop('chunk_text')
        embedding: list = kwargs.pop('embedding')
        start_pos: int = kwargs.pop('start_pos')
        end_pos: int = kwargs.pop('end_pos')
        tokens: int = kwargs.pop('tokens')
        metadata: dict = kwargs.pop('metadata')
        chunk = DocumentChunk(
            document_id=document_id,
            chunk_text=chunk_text,
            embedding=embedding,
            start_pos=start_pos,
            end_pos=end_pos,
            tokens=tokens,
            meta_info=metadata,
        )
        self.db.add(chunk)
        self.db.commit()
        self.db.refresh(chunk)
        return chunk,

    def query(self, embedding: list, top_k: int = 5):
        sql = text("""
                   SELECT id,
                          document_id,
                          chunk_text,
                          meta_info,
                          embedding <-> CAST(:emb AS vector) AS distance
                   FROM document_chunks
                   ORDER BY embedding <-> CAST(:emb AS vector) LIMIT :k
                   """)
        rows = self.db.execute(
            sql,
            {"k": top_k, "emb": embedding}
        )
        return rows
