from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+psycopg2://postgres:postgres@localhost:5432/research_agent"
    EMBEDDING_MODEL_NAME: str = "sentence-transformers/all-mpnet-base-v2"
    EMBEDDING_DIM: int = 768
    LLM_SERVER_URL: str = "http://localhost:8080"
    PG_VECTOR_DIM: int = 768
    SECRET_KEY: str = "change-me-to-a-secure-random-key"
    REDIS_URL: str = "redis://localhost:6379/0"
    POSTGRES_USER: str
    POSTGRES_DB: str
    POSTGRES_PASSWORD: str

    class Config:
        env_file = ".env"
        extra = "allow"


settings = Settings()
