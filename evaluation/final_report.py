import json

input_file = "experiments/run_003/final_score.json"
output_file = "experiments/run_003/final_report.json"

with open(input_file, "r", encoding="utf-8") as file:
    data = json.load(file)

similarity_scores_list = []
faithfulness_scores_list=[]
coverage_scores_list = []
final_scores_list = []

for item in data:
    similarity_score = item['similarity_score']
    similarity_scores_list.append(similarity_score)

    faithfulness_score = item['faithfulness_score']
    faithfulness_scores_list.append(faithfulness_score)

    coverage_score = item['coverage_score']
    coverage_scores_list.append(coverage_score)

    final_score = item['final_score']
    final_scores_list.append(final_score)


avg_similarity_score = sum(similarity_scores_list)/len(similarity_scores_list)
avg_faithfulness_score = sum(faithfulness_scores_list)/len(faithfulness_scores_list)
avg_coverage_score = sum(coverage_scores_list)/len(coverage_scores_list)
avg_final_score = sum(final_scores_list)/len(final_scores_list)



averages = {
    "average_similarity":avg_similarity_score,
    "average_faithfulness": avg_faithfulness_score,
    "average_coverage": avg_coverage_score,
    "average_final": avg_final_score
}

sorted_data_reverse = sorted(data,key=lambda item: item['final_score'],reverse=True)

best_5 = sorted_data_reverse[:5]

sorted_data = sorted(data,key=lambda item: item['final_score'])

worst_5 = sorted_data[:5]

distributions = {

}

combined_data = {
    "averages": averages,
    "Top_5": best_5,
    "Worst_5": worst_5,
    "distributions": distributions
}

with open(output_file, "w", encoding="utf-8") as file:
    json.dump(combined_data, file, indent=4, ensure_ascii=False)

print("final_report created")