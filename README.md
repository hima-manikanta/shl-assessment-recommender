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
