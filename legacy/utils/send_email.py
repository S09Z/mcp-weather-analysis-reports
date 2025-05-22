import os
import smtplib
import ssl
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

def send_email(subject, body, attachment_path):
    # ดึงค่าจาก environment variables
    sender = os.getenv("EMAIL_SENDER")        # ex: your_email@gmail.com
    password = os.getenv("EMAIL_PASSWORD")    # ex: your App Password (16 ตัว)
    recipient = os.getenv("EMAIL_RECIPIENT")  # ex: recipient@gmail.com

    if not sender or not password or not recipient:
        raise ValueError("Environment variables EMAIL_SENDER, EMAIL_PASSWORD, or EMAIL_RECIPIENT not set.")

    # สร้าง Email Message
    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = recipient
    msg["Subject"] = subject
    msg.set_content(body)

    # แนบไฟล์ (เช่น .png)
    if attachment_path:
        with open(attachment_path, "rb") as f:
            file_data = f.read()
            file_name = os.path.basename(attachment_path)
            msg.add_attachment(file_data, maintype="image", subtype="png", filename=file_name)

    # ใช้ SMTP SSL (port 465) กับ Gmail
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender, password)
        server.send_message(msg)
        print("✅ Email sent successfully.")

# ตัวอย่างการใช้งาน
if __name__ == "__main__":
    
    base_dir = os.path.dirname(__file__)
    attachment_path = os.path.abspath(os.path.join(base_dir, "..", "reports", "visualize", "test_report.png"))

    send_email(
        subject="รายงานวิเคราะห์อากาศ",
        body="แนบไฟล์รายงานเป็นภาพ .png ครับ",
        attachment_path=attachment_path  # เปลี่ยนเป็น path จริงของไฟล์ที่คุณมี
    )
