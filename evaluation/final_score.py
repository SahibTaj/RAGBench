import json

input_file = "experiments/run_003/coverage_score.json"
output_file = "experiments/run_003/final_score.json"

with open(input_file,"r", encoding="utf-8") as file:
    data = json.load(file)

for item in data:
    exact_match_score = item["exact_match_score"]
    similarity_score = item["similarity_score"]
    faithfulness_score = item["faithfulness_score"]
    coverage_score = item["coverage_score"]

    final_score = (exact_match_score + similarity_score + faithfulness_score + coverage_score)/4

    item["final_score"] = round(final_score,4)

print("final score calculated")

with open(output_file,"w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

print("final_score created")