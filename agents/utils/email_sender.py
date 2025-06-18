import smtplib
from email.message import EmailMessage

EMAIL_USER = "sharmaranjana953@gmail.com"
EMAIL_PASS = "vsvqcocncnqrddiv"

def send_email(subject, body, to_email):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject.strip()
    msg['From'] = EMAIL_USER
    msg['To'] = to_email.strip().replace('\n', '').replace('\r', '')

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_USER, EMAIL_PASS)
            smtp.send_message(msg)
        print("✅ Email sent successfully.")
        return True
    except Exception as e:
        print("❌ Email failed:", e)
        return False
