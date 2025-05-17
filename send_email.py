import smtplib
from email.message import EmailMessage

def send_email_with_ics(to_email, ics_file, subject="Today's Birthdays", body="Attached is today's birthday reminder."):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = "your_email@gmail.com"
    msg['To'] = to_email
    msg.set_content(body)

    with open(ics_file, 'rb') as f:
        msg.add_attachment(f.read(), maintype='application', subtype='octet-stream', filename=ics_file)

    # Gmail SMTP Example
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login("your_email@gmail.com", "your_app_password")
        smtp.send_message(msg)
