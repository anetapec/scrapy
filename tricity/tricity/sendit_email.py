import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from pipelines import MongoDBPipeline


# bart.gawron@gmail.com

port = 465
smtp_serwer = 'smtp.gmail.com'
sender = 'aneta.gawron85@gmail.com'
#recipient = 'bart.gawron@gmail.com'

recipient = 'aneta.gawron85@gmail.com'
password = os.getenv('API_KEY')
subject = "Houses and flats for sale today"

contents1 = """<b> Hello. </b>
<h6>In attachments I am sending houses and apartments that have been put up for sale today. </h6>"""
contents2 = """Kind regards."""
message = MIMEMultipart()
message["From"] = sender
message["To"] = recipient
message["Subject"] = subject

# add attachment
message.attach(MIMEText(contents1, "html"))
message.attach(MIMEText(contents2, "plain"))

#name_att1 = 'flats_' + MongoDBPipeline.set_scrapping_date() + '.csv'
#tricity/tricity/flats2flats2023-06-17 21:19:21.csv
att1 = MIMEText(open('/home/aneta/software/repos/scrapy/tricity/tricity/flats2023-06-17 21:19:21.csv', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename="flats_17-06-2023.csv"'
message.attach(att1)

att2 = MIMEText(open('/home/aneta/software/repos/scrapy/tricity/tricity/houses2023-06-17 21:10:58.csv', 'rb').read(), 'base64', 'utf-8')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="houses_17-06-2023.csv"'
message.attach(att2)

text = message.as_string()

ssl_connection = ssl.create_default_context()

try:
    with smtplib.SMTP_SSL(smtp_serwer, port, context=ssl_connection) as serwer:
        serwer.login(sender, password)
        serwer.sendmail(sender, recipient, text)
        print("Successffully sent email")
except  Exception as Error:
    print("Unable to send email")

