from sentence_transformers import SentenceTransformer
from config import EMBEDDING_MODEL

embedding_model = EMBEDDING_MODEL

def get_embedding(text):
    
    embedded_chunks = embedding_model.encode(text)

    return embedded_chunks

def generate_embeddings(chunks):
    
    
    text = [chunk.page_content for chunk in chunks]

    embeddings = get_embedding(text)    

    print("embedding done")

    return embeddings

