import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000/recommend"

st.set_page_config(page_title="SHL Assessment Recommender", layout="centered")

st.title("SHL Assessment Recommender")
st.write("Paste a job description, query, or URL to get recommended SHL assessments.")

query = st.text_area("Job Description / Query / URL", height=180)

if st.button("Get Recommendations"):
    if not query.strip():
        st.warning("Please enter a query.")
    else:
        with st.spinner("Finding best assessments..."):
            try:
                resp = requests.post(API_URL, json={"query": query})
                resp.raise_for_status()

                recs = resp.json()["recommendations"]

                if not recs:
                    st.info("No recommendations found.")
                else:
                    df = pd.DataFrame(recs)
                    df.columns = ["Assessment Name", "Assessment URL"]
                    st.success(f"Found {len(df)} assessments")
                    st.dataframe(df, use_container_width=True)

            except Exception as e:
                st.error(f"Error: {e}")
