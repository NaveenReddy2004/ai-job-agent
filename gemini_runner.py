import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_KEY"))

def generate_cover_letter(resume_text, job_title, company):
    prompt = f"""
    Based on the resume:
    {resume_text}

    Write a personalized short cover letter for a {job_title} role at {company}.
    """
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text.strip()
