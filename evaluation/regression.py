import json
import os


BASELINE_RUN = "run_002"
CANDIDATE_RUN = "run_003"

if not os.path.exists(f"experiments/{BASELINE_RUN}/final_report.json"):
    print("Baseline report not found")
    exit()

if not os.path.exists(f"experiments/{CANDIDATE_RUN}/final_report.json"):
    print("Candidate report not found")
    exit()

with open(f"experiments/{BASELINE_RUN}/final_report.json", "r", encoding="utf-8") as file2:
    data2 = json.load(file2)
    averages2 = data2["averages"]

average_similarity_score2 = averages2["average_similarity"]
average_faithfulness_score2 = averages2["average_faithfulness"]
average_coverage_score2 = averages2["average_coverage"]
average_final_score2 = averages2["average_final"]

with open(f"experiments/{CANDIDATE_RUN}/final_report.json", "r", encoding="utf-8") as file3:
    data3 = json.load(file3)
    averages3 = data3["averages"]

average_similarity_score3 = averages3["average_similarity"]
average_faithfulness_score3 = averages3["average_faithfulness"]
average_coverage_score3 = averages3["average_coverage"]
average_final_score3 = averages3["average_final"]


similarity_delta = average_similarity_score3 - average_similarity_score2
faithfulness_delta = average_faithfulness_score3 - average_faithfulness_score2
coverage_delta = average_coverage_score3 - average_coverage_score2
final_delta = average_final_score3 - average_final_score2

if final_delta > 0:
    status = "IMPROVED"

elif final_delta < 0:
    status = "REGRESSED"

else:
    status = "NO_CHANGE"

regression_report = {
    "baseline_run": BASELINE_RUN,
    "candidate_run": CANDIDATE_RUN,

    "metrics": {
        "similarity_delta": round(similarity_delta, 4),
        "faithfulness_delta": round(faithfulness_delta, 4),
        "coverage_delta": round(coverage_delta, 4),
        "final_score_delta": round(final_delta, 4)
    },

    "status": status
}

with open(f"experiments/{CANDIDATE_RUN}/regression_report.json","w", encoding="utf-8") as file:
    json.dump(
        regression_report,
        file,
        indent=4,
        ensure_ascii=False
    )

print("=" * 50)
print(f"Status: {status}")
print(f"Similarity Delta: {similarity_delta:.4f}")
print(f"Faithfulness Delta: {faithfulness_delta:.4f}")
print(f"Coverage Delta: {coverage_delta:.4f}")
print(f"Final Score Delta: {final_delta:.4f}")
print("=" * 50)

print("regression_report created")