from sentence_transformers import SentenceTransformer, util
import json
from config import EMBEDDING_MODEL

model = EMBEDDING_MODEL

input_file = "experiments/run_003/faithfulness_score.json"
output_file = "experiments/run_003/coverage_score.json"

with open(input_file, "r", encoding="utf-8") as file:
    data = json.load(file)

print("coverage score started")


for item in data:
    prediction = item["prediction"],
    ground_truth = item["ground_truth"]

    prediction_embedding = model.encode(prediction, convert_to_tensor=True)
    ground_truth_embedding = model.encode(ground_truth, convert_to_tensor=True)

    score = util.cos_sim(prediction_embedding, ground_truth_embedding)

    item["coverage_score"] = round(score.item(),4)

print("coverage score ended")

with open(output_file,"w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

print("coverage_score created")