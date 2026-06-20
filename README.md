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

## Project folder structure
<img width="305" height="533" alt="image" src="https://github.com/user-attachments/assets/a6fac042-5eb5-495f-b0ae-f09c24eb0d4b" />  
<img width="297" height="842" alt="image" src="https://github.com/user-attachments/assets/fdae45d5-85cf-484a-b288-984165be3b6f" />  
<img width="308" height="856" alt="image" src="https://github.com/user-attachments/assets/afa9bd2d-0b80-42be-b78d-6bbec0d03058" />


## output
<img width="872" height="682" alt="image" src="https://github.com/user-attachments/assets/c7978905-348e-4665-b4e9-ffac7648545b" />
<img width="886" height="572" alt="image" src="https://github.com/user-attachments/assets/6935a817-9045-42ee-a811-a226f23b0238" />
<img width="882" height="346" alt="image" src="https://github.com/user-attachments/assets/c679f80a-e9e8-4a33-a3f0-1f54b28893d9" />
<img width="877" height="341" alt="image" src="https://github.com/user-attachments/assets/a5cf985c-fcce-4289-a043-c5d0cf1c05f8" />
<img width="876" height="350" alt="image" src="https://github.com/user-attachments/assets/2bec1e32-ba80-4e54-8121-1b3e8c58f2b9" />



## Author

Sahib Taj Singh
