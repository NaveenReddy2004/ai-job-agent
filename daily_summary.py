import smtplib
from email.message import EmailMessage
import os

def send_applied_email(jobs):
    user = os.getenv("GMAIL_USER")
    password = os.getenv("GMAIL_PASS")
    
    msg = EmailMessage()
    msg["Subject"] = "📌 Applied Job Summary"
    msg["From"] = user
    msg["To"] = user

    content = "\n\n".join([f"{job['Job Title']} at {job['Company']}\n{job['Job Link']}\n{job['Cover Letter']}" for job in jobs])
    msg.set_content(content)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(user, password)
        smtp.send_message(msg)
