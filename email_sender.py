import smtplib # Python’s built-in library to send emails using SMTP
from email.mime.multipart import MIMEMultipart # lets you create an email that can contain text + attachments.
from email.mime.base import MIMEBase # defines an attachment type (e.g., file, image, PDF)
from email import encoders # helps encode the attachment so email servers can understand it
import os
from dotenv import load_dotenv

def send_email(to_email, subject, body, file_path):
    """Sends an email with the .ics file attached."""

    load_dotenv()
    sender_email = os.getenv("EMAIL_USER")
    sender_password = os.getenv("EMAIL_PASS")            

    # Email setup
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = to_email
    msg["Subject"] = subject

    # Attach the file
    with open(file_path, "rb") as f: # opens file in binary mode
        part = MIMEBase("application", "octet-stream")
        part.set_payload(f.read()) # reads the file’s contents into the email
        encoders.encode_base64(part) # encodes the file so it can travel safely over email
        part.add_header("Content-Disposition", f"attachment; filename={file_path}") # gives the file a name in the email attachment
        msg.attach(part) # attaches the file to the email

    # Connect to Gmail SMTP
    with smtplib.SMTP("smtp.gmail.com", 465) as server:
        server.ehlo()
        server.starttls() # upgrade the connection to secure (encrypted)
        server.login(sender_email, sender_password) # logs in to your email account
        server.send_message(msg) # sends the email
 
    print("Email sent successfully!")
