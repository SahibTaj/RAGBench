from rag.embedder import get_embedding
from config import TOP_K

def retrieve_documents(question, collection):
    
    question_vector = [get_embedding(question)]
    
    result = collection.query(
        query_embeddings = question_vector,
        n_results = TOP_K
    )

    # print(result.keys())


    # print("data retrieved")

    return result

def retrieved_chunks(result):
    retrieved_chunks = result["documents"][0]

    return retrieved_chunks