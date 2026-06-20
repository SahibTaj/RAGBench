import json
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer(
        "sentence-transformers/all-MiniLM-L6-v2"
    )

input_file = "experiments/run_003/exact_match_score.json"
output_file = "experiments/run_003/semantic_similarity_score.json"

with open(input_file, "r", encoding="utf-8") as file:
    data = json.load(file)

print("semantic similarity started")

for item in data:
    question = item["question"]
    ground_truth = item["ground_truth"]
    prediction = item["prediction"]

    if not ground_truth or not prediction:
        item["similarity_score"] = 0.0
        continue

    ground_truth_embedding = model.encode(ground_truth, convert_to_tensor=True)
    prediction_embedding = model.encode(prediction, convert_to_tensor=True)

    score = util.cos_sim(ground_truth_embedding, prediction_embedding)

    item["similarity_score"] = round(score.item(),4)

print("semantic similarity done")

with open(output_file,"w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

print("semantic_similarity_score created")