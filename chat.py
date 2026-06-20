from rag.retriever import retrieve_documents
from rag.generator import generate_answer
from rag.vectordb import load_collection

collection = load_collection()

question = input("Ask a question: ")

results = retrieve_documents(
    question,
    collection
)

answer = generate_answer(
    question,
    results
)

print("\nRetrieved Chunks:\n")
print(results["documents"])

print("\nAnswer:\n")
print(answer)
