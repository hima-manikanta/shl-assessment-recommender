# SHL Assessment Recommendation System  
### A Web-Based RAG Tool for Intelligent Assessment Matching

🔗 **Live Application**  
https://shl-assessment-recommender-manu.streamlit.app/

---

## Project Overview

This project is a **web-based assessment recommendation system** built using SHL’s public product catalog.  
It helps recruiters and hiring managers **identify the most relevant SHL Individual Test Solutions** based on a job description, hiring requirement, or free-text query.

The system follows a **Retrieval-Augmented Generation (RAG)** approach by combining:
- semantic search over SHL assessments, and  
- Large Language Model (LLM)–based query understanding.

The solution is designed to be **simple, explainable, evaluable, and fully functional** using free and open-source tools.

---

## Key Features

- Scrapes and stores **SHL Individual Test Solutions** from the official SHL catalog  
- Supports **job descriptions, hiring queries, and free text**  
- Uses **Sentence Transformers + FAISS** for semantic retrieval  
- Uses **Gemini LLM** for query understanding and skill extraction  
- Returns **5–10 relevant SHL assessments** with direct URLs  
- Includes **Recall@10 evaluation** on provided training data  
- Fully deployed and accessible via a public web interface  

---

## Live Demo

You can try the system here:

👉 **Web App URL**  
https://shl-assessment-recommender-manu.streamlit.app/

**Example query:**
```

Looking to hire mid-level Java developers with strong communication skills

```

The app returns a ranked list of relevant SHL assessments.

---

## System Architecture

### 1. Data Collection
- Scraped SHL **Individual Test Solutions** (pre-packaged job solutions excluded)
- Extracted:
  - Assessment name  
  - Description  
  - Category  
  - Test type  
  - Assessment URL  
- Final dataset contains **~385 assessments**

### 2. Data Processing & Indexing
- Cleaned and deduplicated catalog data  
- Created a combined text field using name, description, and category  
- Generated embeddings using:
```

sentence-transformers/all-MiniLM-L6-v2

```
- Stored embeddings in a **FAISS vector index** for efficient similarity search

### 3. Query Understanding (LLM)
- User queries are analyzed using **Google Gemini**
- Extracts:
- Technical skills  
- Soft skills  
- Assessment focus (Knowledge / Skills / Mixed)  
- This information guides ranking and recommendation logic

### 4. Retrieval & Ranking
- Query embedding is compared against FAISS index  
- Top-K candidates are retrieved  
- Results are re-ranked to balance technical and behavioral assessments  
- Final output contains **5–10 SHL Individual Test Solutions**

### 5. Frontend & Deployment
- Built using **Streamlit**
- Backend recommendation logic reused directly inside the app
- Deployed on **Streamlit Cloud (free)**

---

## Evaluation

- Evaluation metric: **Mean Recall@10**
- Evaluated on the provided Train-Set queries
- Achieved **Recall@10 ≈ 0.108**

### Evaluation Notes
Lower recall is expected due to:
- Exact URL matching requirements
- Missing or limited descriptions for some assessments
- High semantic overlap across SHL assessments

Despite this, the system consistently produces **semantically relevant and practically useful recommendations**, which can be validated through manual inspection.

---

## Repository Structure

```

shl-assessment-recommender/
├── api/                 # Recommendation logic
├── data/                # Scraped and cleaned SHL catalog
├── embeddings/          # FAISS index and embedding scripts
├── evaluation/          # Recall@10 evaluation
├── frontend/            # Streamlit web app
├── outputs/             # predictions.csv
├── requirements.txt
└── README.md

````

---

## Running Locally (Optional)

```bash
pip install -r requirements.txt
streamlit run frontend/app.py
````

---

## Submission Artifacts

* **Web App URL:**
  [https://shl-assessment-recommender-manu.streamlit.app/](https://shl-assessment-recommender-manu.streamlit.app/)

* **Source Code:**
  This GitHub repository

* **Predictions File:**
  `firstname_lastname.csv`

* **Approach Document:**
  2-page PDF outlining system design and evaluation

---

## Final Notes

This project prioritizes:

* clarity of system design,
* correctness of retrieval logic,
* responsible use of LLMs,
* and transparent evaluation.

The solution meets all requirements of the **SHL GenAI Assessment Recommendation** task and is ready for review and evaluation.

---
