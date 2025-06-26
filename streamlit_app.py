# Streamlit UI code (replace this with your latest streamlit_app.py)
import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="AI Job Agent", layout="centered")

st.title("📄 Resume Uploader & Job Tracker")

uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])
if uploaded_file:
    with open("resume.pdf", "wb") as f:
        f.write(uploaded_file.read())
    st.success("✅ Resume uploaded successfully!")

st.subheader("📊 Applied Jobs")
try:
    df = pd.read_csv("applied_jobs.csv", names=["timestamp", "Job Title", "Company", "Job Link", "Cover Letter", "status"], skiprows=1)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values("timestamp", ascending=False)
    st.dataframe(df[["timestamp", "Job Title", "Company", "Job Link"]])
except FileNotFoundError:
    st.info("No applications recorded yet.")
