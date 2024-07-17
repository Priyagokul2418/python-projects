import ssl
import smtplib
from email.message import EmailMessage

email_sender = "gokulpriya391@gmail.com"
email_password = "ljcx rdyt ituh jlrl"  # Update with your actual email password
email_receiver = "priyagokul854@gmail.com"

subject = "Project"
body = """
Welcome to my project.
"""

msg = EmailMessage()
msg.set_content(body)
msg['Subject'] = subject
msg['From'] = email_sender
msg['To'] = email_receiver

context = ssl.create_default_context()

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.send_message(msg)
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email. Error: {e}")
