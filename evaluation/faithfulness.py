from sentence_transformers import SentenceTransformer, util
import json

model = SentenceTransformer(
        "sentence-transformers/all-MiniLM-L6-v2"
    )

input_file = "experiments/run_003/semantic_similarity_score.json"
output_file = "experiments/run_003/faithfulness_score.json"

with open(input_file, "r", encoding="utf-8") as file:
    data = json.load(file)

combined_context = []

print("faithfullness score started")

for item in data:
    prediction = item["prediction"],
    retrieved_chunks = item["retrieved_chunks"]

    combined_context = " ".join(retrieved_chunks)

    prediction_embedding = model.encode(prediction, convert_to_tensor=True)
    combined_context_embedding = model.encode(combined_context, convert_to_tensor=True)

    score = util.cos_sim(prediction_embedding, combined_context_embedding)

    item["faithfulness_score"] = round(score.item(),4)

print("faithfullness score ended")

with open(output_file, "w", encoding="utf-8") as file:
    json.dump(data, file,indent=4, ensure_ascii=False)

print("faithfulness_score created")