import json

input_file = "experiments/run_003/eval_results.json"
output_file = "experiments/run_003/exact_match_score.json"

with open(input_file,"r", encoding="utf-8") as file:
    data = json.load(file)

exact_match_score=[]
print("exact_match started")
for item in data:
    question = item["question"]
    ground_truth = item["ground_truth"]
    prediction = item["prediction"]

    if ground_truth == prediction:
        match_score = 1
    else:
        match_score = 0
    
    item["exact_match_score"] = match_score
    
print("exact_match ended")

with open(output_file, "w",encoding="utf-8") as file:
    json.dump(data,file, indent=4)
    
print("exact_match_score created")