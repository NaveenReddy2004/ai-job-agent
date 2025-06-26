import fitz  # PyMuPDF

def load_resume_text(file_path='Naveen_Resume(2).pdf'):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

