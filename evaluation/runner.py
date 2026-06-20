from rag.retriever import retrieve_documents
from rag.vectordb import load_collection
from rag.generator import generate_answer
from rag.retriever import retrieved_chunks
import json

with open("data/test_questions.json","r") as f:
    questions = json.load(f)

collection = load_collection()

output_file = "experiments/run_003/eval_results.json"

json_output = []

print("runner started")

for item in questions:

    question = item["question"]
    
    ground_truth = item["ground_truth"]

    results = retrieve_documents(question,collection)

    answer = generate_answer(question, results)

    chunks = retrieved_chunks(results)

    # print("\nQuestion:", question)
    # print("Ground Truth:", ground_truth)
    # print("Prediction:", answer)
    # print("-" * 50)

    data = {
        "question": question,
        "ground_truth": ground_truth,
        "prediction": answer,
        "retrieved_chunks": chunks
    }

    json_output.append(data)

print("runner ended")

with open(output_file, "w",encoding="utf-8") as file:
    json.dump(json_output, file, indent=4)

print("eval_results created")