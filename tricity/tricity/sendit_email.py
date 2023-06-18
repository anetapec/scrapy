from pipelines import MongoDBPipeline
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os 
import re

class Mail:

    def __init__(self):
        self.port = 465
        self.smtp_serwer = 'smtp.gmail.com'
        self.sender = 'aneta.gawron85@gmail.com'
        self.password = os.getenv('API_KEY')
        self.recipient = 'aneta.gawron85@gmail.com'

    def send(self):
        ssl_context = ssl.create_default_context()
        service = smtplib.SMTP_SSL(self.smtp_serwer, self.port, context=ssl_context)
        service.login(self.sender, self.password)

        mail = MIMEMultipart()
        mail['Subject'] = 'Houses and flats for sale today'
        mail['From'] = self.sender
        mail['To'] = self.recipient

        contents = """<b> Hello. </b>
        <h6>In attachments I am sending houses and apartments that have been put up for sale today. </h6>"""

        mail.attach(MIMEText(contents, "html"))

        name_att1 = MongoDBPipeline()
        #att1 = name_att1.open_spider(spider='flatsspider'.filename)

        att1_to_send = name_att1.set_name_file(spider_mongo_collection='flats')
        att1_to_send_convert = re.sub("[a-zA-Z0-9]-[0-9]-[0-9]", "", att1_to_send)
        #att1 = name_att1.open_spider(spider='flatsspider'(self.filename))
        att1_to_send_convert = MIMEText(open(name_att1, 'rb').read(), 'base64', 'utf-8')
        att1_to_send_convert["Content-Type"] = 'application/octet-stream'
        att1_to_send_convert["Content-Disposition"] = f'attachment; filename={name_att1}'
        mail.attach(att1_to_send_convert)

        try:
            service.sendmail(self.sender, self.recipient, mail.as_string())
            print("Successffully sent email")
        except  Exception as Error:
            print("Unable to send email")

email = Mail()
email.send()
