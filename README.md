# Regression-Safe RAG Evaluation Platform

## Overview

A framework for evaluating Retrieval-Augmented Generation (RAG) systems using automated quality metrics, experiment tracking, and regression testing.

The platform enables systematic benchmarking of RAG pipelines by measuring retrieval quality, answer quality, faithfulness, and overall performance across multiple experiments.

## Features

* PDF document ingestion
* Recursive chunking
* Embedding generation using Sentence Transformers
* ChromaDB vector database
* Semantic retrieval
* LLM-based answer generation
* Exact Match evaluation
* Semantic Similarity evaluation
* Faithfulness evaluation
* Coverage evaluation
* Weighted Final Score
* Experiment tracking
* Regression testing between runs

## Architecture

PDF Documents
↓
Document Loader
↓
Chunking
↓
Embedding Model
↓
ChromaDB
↓
Retriever
↓
LLM Generator
↓
Evaluation Pipeline
↓
Experiment Reports

## Evaluation Metrics

### Exact Match

Measures whether generated answers exactly match ground truth answers.

### Semantic Similarity

Measures semantic similarity between generated answers and reference answers using Sentence Transformers.

### Faithfulness

Measures whether generated answers are supported by retrieved context.

### Coverage

Measures how much of the expected information is covered in the generated answer.

### Final Score

Final Score = Weighted combination of:

* Semantic Similarity
* Faithfulness
* Coverage

<img width="262" height="287" alt="image" src="https://github.com/user-attachments/assets/3cf4cf42-aeac-4cc3-b072-c7becf4ae1ba" />


## Experiment Tracking

Every experiment automatically creates:

experiments/
├── run_001/
├── run_002/
├── run_003/

Each run stores:

* eval_results.json
* exact_match_score.json
* semantic_similarity_score.json
* faithfulness_score.json
* coverage_score.json
* final_score.json
* final_report.json

<img width="298" height="267" alt="image" src="https://github.com/user-attachments/assets/bcdf894c-2dfc-43a5-b970-3898cb4b03de" />

## Regression Testing

The platform supports comparison between experiments.

Example:

Run 002
Chunk Size: 800
Chunk Overlap: 100
<img width="763" height="283" alt="image" src="https://github.com/user-attachments/assets/ebf356bd-43d8-4068-aa9b-c4bb2dc63873" />

vs

Run 003
Chunk Size: 100
Chunk Overlap: 50
<img width="721" height="282" alt="image" src="https://github.com/user-attachments/assets/0818318d-11a2-4b1c-9108-3fef088401db" />

The regression module calculates:

* Similarity Delta
* Faithfulness Delta
* Coverage Delta
* Final Score Delta

and reports:

* IMPROVED
* REGRESSED
* NO_CHANGE

<img width="506" height="307" alt="image" src="https://github.com/user-attachments/assets/01e843e5-ab34-4b46-9b24-2cb45db10a93" />

## Tech Stack

* Python
* LangChain
* ChromaDB
* Sentence Transformers
* HuggingFace
* Groq API
* JSON

## Installation

```bash
git clone <repo_url>

cd Regression-Safe-RAG-Evaluation-Platform

pip install -r requirements.txt
```

## Usage

Build Index

```bash
python build_index.py
```

Run Evaluation Pipeline

```bash
python main.py
```

Run Regression Analysis

```bash
python -m evaluation.regression
```

## Example Results

| Metric       | Score  |
| ------------ | ------ |
| Similarity   | 0.3997 |
| Faithfulness | 0.3944 |
| Coverage     | 0.3997 |
| Final Score  | 0.2984 |


## Author

Sahib Taj Singh
