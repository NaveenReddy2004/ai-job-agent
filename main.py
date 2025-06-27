from job_scraper import scrape_jobs
from gemini_runner import generate_cover_letter
from resume_loader import load_resume_text
from daily_summary import send_applied_email
import pandas as pd
import datetime

resume_text = load_resume_text()

jobs = scrape_jobs("internships for machine learning", num_results=5)

for job in jobs:
    job["Cover Letter"] = generate_cover_letter(resume_text, job["Job Title"], job["Company"])

applied_df = pd.DataFrame(jobs)
applied_df["timestamp"] = datetime.datetime.now().isoformat()
applied_df["status"] = "Applied"
applied_df.to_csv("applied_jobs.csv", mode='a', header=False, index=False)

send_applied_email(jobs)

if __name__ == "__main__":
    try:
        resume_text = load_resume_text() 
        print("Resume Loaded Successfully!\n")
        print(resume_text[:1000])  
    except FileNotFoundError as e:
        print(f"{e}")
