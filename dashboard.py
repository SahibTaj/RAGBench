import streamlit as st
import pandas as pd
import json
import os

st.set_page_config(
    page_title="RAGBench Dashboard",
    layout="wide"
)

st.title("📊 Regression-Safe RAG Evaluation Platform")

EXPERIMENTS_DIR = "experiments"

runs = sorted(
    [
        run
        for run in os.listdir(EXPERIMENTS_DIR)
        if run.startswith("run_")
    ]
)

experiment_data = []

for run in runs:

    experiment_file = os.path.join(
        EXPERIMENTS_DIR,
        run,
        "experiment_info.json"
    )

    report_file = os.path.join(
        EXPERIMENTS_DIR,
        run,
        "final_report.json"
    )

    if not (
        os.path.exists(experiment_file)
        and os.path.exists(report_file)
    ):
        continue

    with open(experiment_file, "r", encoding="utf-8") as f:
        experiment_info = json.load(f)

    with open(report_file, "r", encoding="utf-8") as f:
        report = json.load(f)

    averages = report["averages"]

    experiment_data.append({
        "Run": run,
        "Chunk Size": experiment_info["CHUNK_SIZE"],
        "Chunk Overlap": experiment_info["CHUNK_OVERLAP"],
        "Similarity": averages["average_similarity"],
        "Faithfulness": averages["average_faithfulness"],
        "Coverage": averages["average_coverage"],
        "Final Score": averages["average_final"]
    })

df = pd.DataFrame(experiment_data)

st.header("Experiment Comparison")

st.dataframe(
    df,
    use_container_width=True
)

best_run = df.loc[df["Final Score"].idxmax()]

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Experiments",
        len(df)
    )

with col2:
    st.metric(
        "Best Run",
        best_run["Run"]
    )

with col3:
    st.metric(
        "Best Final Score",
        round(best_run["Final Score"], 4)
    )

st.header("Performance Comparison")

st.bar_chart(
    df.set_index("Run")[
        [
            "Similarity",
            "Faithfulness",
            "Coverage",
            "Final Score"
        ]
    ]
)

st.sidebar.header("Run Details")

selected_run = st.sidebar.selectbox(
    "Select Run",
    runs
)

selected_info_file = os.path.join(
    EXPERIMENTS_DIR,
    selected_run,
    "experiment_info.json"
)

selected_report_file = os.path.join(
    EXPERIMENTS_DIR,
    selected_run,
    "final_report.json"
)

with open(selected_info_file, "r", encoding="utf-8") as f:
    selected_info = json.load(f)

with open(selected_report_file, "r", encoding="utf-8") as f:
    selected_report = json.load(f)

st.header(f"Details: {selected_run}")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Configuration")

    st.write(
        f"Chunk Size: {selected_info['CHUNK_SIZE']}"
    )

    st.write(
        f"Chunk Overlap: {selected_info['CHUNK_OVERLAP']}"
    )

with col2:
    st.subheader("Metrics")

    averages = selected_report["averages"]

    st.write(
        f"Similarity: {averages['average_similarity']:.4f}"
    )

    st.write(
        f"Faithfulness: {averages['average_faithfulness']:.4f}"
    )

    st.write(
        f"Coverage: {averages['average_coverage']:.4f}"
    )

    st.write(
        f"Final Score: {averages['average_final']:.4f}"
    )

regression_file = os.path.join(
    EXPERIMENTS_DIR,
    selected_run,
    "regression_report.json"
)

if os.path.exists(regression_file):

    with open(
        regression_file,
        "r",
        encoding="utf-8"
    ) as f:
        regression = json.load(f)

    st.header("Regression Analysis")

    st.success(
        f"Status: {regression['status']}"
    )

    metrics = regression["metrics"]

    st.write(
        f"Similarity Delta: {metrics['similarity_delta']}"
    )

    st.write(
        f"Faithfulness Delta: {metrics['faithfulness_delta']}"
    )

    st.write(
        f"Coverage Delta: {metrics['coverage_delta']}"
    )

    st.write(
        f"Final Score Delta: {metrics['final_score_delta']}"
    )