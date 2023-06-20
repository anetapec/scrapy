from tricity import *
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



class Mail:

    def __init__(self):
        self.port = 465
        self.smtp_serwer = 'smtp.gmail.com'
        self.sender = 'aneta.gawron85@gmail.com'
        self.password = 'wgyufumaoypulziu'
        #self.password = os.getenv('API_KEY')
        self.recipient = 'aneta.gawron85@gmail.com'

    def send(self):
        ssl_connection = ssl.create_default_context()
        service = smtplib.SMTP_SSL(self.smtp_serwer, self.port, context=ssl_connection)
        service.login(self.sender, self.password)
        mail = MIMEMultipart()
        mail['Subject'] = 'Houses and flats for sale today'
        mail['From'] = self.sender
        mail['To'] = self.recipient

        contents = """<b> Hello. </b>
        <h6>In attachments I am sending houses and apartments that have been put up for sale today. </h6>"""

        mail.attach(MIMEText(contents, "html"))

        #### Adding attachments :

        

        # name_att1 = MongoDBPipeline()
        # #att1 = name_att1.open_spider(spider='flatsspider'.filename)

        # att1_to_send = name_att1.set_name_file(spider_mongo_collection='flats')
        # #att1 = name_att1.open_spider(spider='flatsspider'(self.filename))
        # att1_to_send = MIMEText(open(name_att1, 'rb').read(), 'base64', 'utf-8')
        # att1_to_send["Content-Type"] = 'application/octet-stream'
        # att1_to_send["Content-Disposition"] = f'attachment; filename={name_att1}'
        # mail.attach(att1_to_send)

        try:
            service.sendmail(self.sender, self.recipient, mail.as_string())
            print("Successffully sent email")
        except  Exception as Error:
            print("Unable to send email")
    