import smtplib # Python’s built-in library to send emails using SMTP
from email.mime.multipart import MIMEMultipart # lets you create an email that can contain text + attachments.
from email.mime.base import MIMEBase # defines an attachment type (e.g., file, image, PDF)
from email import encoders # helps encode the attachment so email servers can understand it

def send_email(to_email, subject, body, file_path):
    """Sends an email with the .ics file attached."""

    from_email = "your_email@example.com"   # CHANGE THIS
    password = "your_password"              # CHANGE THIS

    # Email setup
    msg = MIMEMultipart()
    msg["From"] = from_email
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
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls() # upgrade the connection to secure (encrypted)
        server.login(from_email, password) # logs in to your email account
        server.send_message(msg) # sends the email
 
    print("Email sent successfully!")
