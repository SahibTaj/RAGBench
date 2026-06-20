from sentence_transformers import SentenceTransformer

EMBEDDING_MODEL = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)
CHUNK_SIZE = 100
CHUNK_OVERLAP = 50
TOP_K = 3

LLM_MODEL = "llama-3.1-8b-instant"
TEMPERATURE = 0