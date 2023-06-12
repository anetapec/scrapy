import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os


port = 465
smtp_serwer = 'smtp.gmail.com'
sender = 'aneta.gawron85@gmail.com'
recipient = 'bart.gawron@gmail.com' #'aneta.gawron85@gmail.com', 
password = os.getenv('API_KEY')
subject = "Email sent a python with attachment"
contents1 = """Text without Html."""
contents2 = """<h1>This is message with HTML.</h1>
<b> This is bold text. </b>
"""
message = MIMEMultipart()
message["From"] = sender
message["To"] = recipient
message["Subject"] = subject

# add attachment
message.attach(MIMEText(contents1, "plain"))
message.attach(MIMEText(contents2, "html"))

att1 = MIMEText(open('flats_for_sale_today.csv', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename="flats_for_sale_today.csv"'
message.attach(att1)

att2 = MIMEText(open('houses_for_sale_today.csv', 'rb').read(), 'base64', 'utf-8')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="houses_for_sale_today.csv"'
message.attach(att2)

text = message.as_string()

ssl_connection = ssl.create_default_context()


with smtplib.SMTP_SSL(smtp_serwer, port, context=ssl_connection) as serwer:
    serwer.login(sender, password)
    serwer.sendmail(sender, recipient, text)

