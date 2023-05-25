import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

port = 465
smtp_serwer = 'smtp.gmail.com'
sender = 'aneta.gawron85@gmail.com'
recipient = 'aneta.gawron85@gmail.com'
password = 'wgyufumaoypulziu'
#haslo = input("Wprowadz swoje hasło: ")
subject = "Text e-mail"
contents1 = """Text without Html."""
contents2 = """<h1>This is message with HTML.</h1>
<b> This is bold text. </b>
"""

file = "password.txt"

message = MIMEMultipart()
message["From"] = sender
message["To"] = recipient
message["Subject"] = subject

# add attachment
message.attach(MIMEText(contents1, "plain"))
message.attach(MIMEText(contents2, "html"))
with open(file, "rb") as f:
    attachment = MIMEBase("application", "octet-stream")
    attachment.set_payload(f.read())

encoders.encode_base64(attachment)

attachment.add_header(
    "Content-Disposition",
    f"attachment; filename= {file}")

message.attach(attachment)
text = message.as_string()

ssl_connection = ssl.create_default_context()


with smtplib.SMTP_SSL(smtp_serwer, port, context=ssl_connection) as serwer:
    serwer.login(sender, password)
    serwer.sendmail(sender, recipient, text)

'''
/home/aneta/software/repos/scrapy/email/password
'''