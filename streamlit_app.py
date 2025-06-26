import streamlit as st
import pandas as pd
import datetime
import fitz  
import os
from job_scraper import scrape_jobs
from gemini_runner import generate_cover_letter
from daily_summary import send_applied_email


st.set_page_config(page_title="AI Job Agent", layout="centered")
st.title("🤖 AI Job Search & Application Agent")

# Upload Resume 
st.subheader("📄 Upload Resume")
uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
resume_text = ""

if uploaded_file:
    with open("resume.pdf", "wb") as f:
        f.write(uploaded_file.read())
    st.success("✅ Resume uploaded")

    # Extract text
    doc = fitz.open("resume.pdf")
    for page in doc:
        resume_text += page.get_text()

    with st.expander("🔍 Preview Extracted Resume"):
        st.write(resume_text)

# Agent Trigger
st.subheader("🚀 Run AI Job Agent")

query = st.text_input("🔍 Job Search Query", value="internships for machine learning")
num_jobs = st.slider("📌 Number of jobs to apply", 1, 10, 5)

if st.button("Apply Now"):

    if not resume_text:
        st.warning("❗ Please upload your resume first.")
    else:
        st.info("🔍 Scraping job listings...")
        jobs = scrape_jobs(query, num_results=num_jobs)

        for job in jobs:
            job["Cover Letter"] = generate_cover_letter(resume_text, job["Job Title"], job["Company"])

        # Save
        applied_df = pd.DataFrame(jobs)
        applied_df["timestamp"] = datetime.datetime.now().isoformat()
        applied_df["status"] = "Applied"
        applied_df.to_csv("applied_jobs.csv", mode='a', header=False, index=False)

        send_applied_email(jobs)

        st.success(f"✅ Applied to {len(jobs)} job(s) successfully!")

# View Applications 
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
    st.info("No applications found yet.")
