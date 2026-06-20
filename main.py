import subprocess
import sys

print("=" * 50)
print("Starting RAG Evaluation Pipeline")
print("=" * 50)

print(f"\nUsing Python: {sys.executable}")

steps = [
    ("Building Index", ["build_index.py"]),
    ("Running Evaluation", ["-m", "evaluation.runner"]),
    ("Calculating Exact Match", ["-m", "evaluation.exact_match"]),
    ("Calculating Semantic Similarity", ["-m", "evaluation.semantic_similarity"]),
    ("Calculating Faithfulness", ["-m", "evaluation.faithfulness"]),
    ("Calculating Coverage", ["-m", "evaluation.coverage"]),
    ("Calculating Final Score", ["-m", "evaluation.final_score"]),
    ("Generating Final Report", ["-m", "evaluation.final_report"]),
    ("Running Regression Analysis", ["-m", "evaluation.regression"]),
]

for step_name, command in steps:

    print(f"\n{'=' * 50}")
    print(step_name)
    print(f"{'=' * 50}")

    result = subprocess.run(
        [sys.executable] + command,
        text=True,
        capture_output=True
    )

    if result.stdout:
        print(result.stdout)

    if result.stderr:
        print(result.stderr)

    if result.returncode != 0:
        print(f"\nFAILED: {step_name}")
        sys.exit(1)

    print(f"\nSUCCESS: {step_name}")

print("\n" + "=" * 50)
print("Pipeline Completed Successfully")
print("=" * 50)