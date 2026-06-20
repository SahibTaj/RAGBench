from rag.loader import load_documents
from rag.chunker import chunk_documents
from rag.embedder import generate_embeddings
from rag.vectordb import store_data


file_paths = ["data/aiayn.pdf",
             "data/rag_for_nlp.pdf"
             ]

all_docs = []

for file_path in file_paths:
    docs = load_documents(file_path)

    for doc in docs:
        doc.metadata["source"] = file_path

    all_docs.extend(docs)


chunks = chunk_documents(all_docs)

embeddings = generate_embeddings(chunks)

store_data(chunks, embeddings)
print(f"Total Chunks Created: {len(chunks)}")
print("index built")