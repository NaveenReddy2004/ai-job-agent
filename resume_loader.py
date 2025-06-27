import os
import fitz

def load_resume_text(file_path="resumes/Naveen_Resume.pdf"):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Resume file not found at: {file_path}")

    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text
