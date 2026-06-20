import chromadb
def store_data(chunks, embeddings):
    
    metadata = [chunk.metadata for chunk in chunks]
    documents = [chunk.page_content for chunk in chunks]
    ids = [f"chunk_{i}" for i in range (len(chunks))]

    client = chromadb.PersistentClient(path="./my_chroma_db")

    try:
        client.delete_collection("rag_documents")
    except:
        pass

    collection = client.create_collection(
        name="rag_documents"
    )

    collection.add(
        ids= ids,
        documents=documents,
        embeddings=embeddings,
        metadatas=metadata
    )

    print("data stored")

    return collection

def load_collection():
    client = chromadb.PersistentClient(
        path="./my_chroma_db"
    )

    collection = client.get_collection(
        name="rag_documents"
    )

    return collection