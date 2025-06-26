import streamlit as st
import pandas as pd
import fitz  # PyMuPDF
from datetime import datetime
import os

st.set_page_config(page_title="AI Job Agent", layout="centered")

st.title("📄 Resume Uploader + 🧠 Job Application Tracker")

# RESUME UPLOADER
st.subheader("📤 Upload Resume (PDF)")
uploaded_file = st.file_uploader("Choose a PDF resume", type="pdf")
if uploaded_file:
    with open("resume.pdf", "wb") as f:
        f.write(uploaded_file.read())
    st.success("✅ Resume uploaded and saved as `resume.pdf`")

    # Optional preview of resume text
    doc = fitz.open("resume.pdf")
    resume_text = ""
    for page in doc:
        resume_text += page.get_text()
    with st.expander("🔍 Preview Resume Text"):
        st.write(resume_text)


# JOB TRACKER 
st.subheader("📊 Applied Jobs Log")
if os.path.exists("applied_jobs.csv"):
    df = pd.read_csv("applied_jobs.csv", names=["Job Title", "Company", "Job Link", "Cover Letter", "timestamp", "status"], skiprows=1)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values("timestamp", ascending=False)

    for _, row in df.iterrows():
        with st.container():
            st.markdown(f"### ✅ {row['Job Title']} at {row['Company']}")
            st.markdown(f"🔗 [Job Link]({row['Job Link']})")
            st.markdown(f"🕒 Applied on: `{row['timestamp']}`")
            with st.expander("📬 View Cover Letter"):
                st.write(row["Cover Letter"])
else:
    st.info("No job applications found yet.")
