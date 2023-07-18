import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from smtplib import SMTPAuthenticationError
from socket import gaierror



class Mail:

    def __init__(self, filename):
        self.port = 465
        self.smtp_serwer = 'smtp.gmail.com'
        self.sender = 'aneta.pecka@gmail.com'
        self.password = 'odryawntjeotfpig'
        #self.password = os.getenv('API_KEY')
        #self.recipient = 'aneta.gawron85@gmail.com'
        #self.recipient = 'aneta.pecka@gmail.com'
        self.recipient = 'bart.gawron@gmail.com'
        self.filename = filename

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

        file_content = open(self.filename, 'rb').read()
        att1_to_send = MIMEText(file_content, 'base64', 'utf-8')
        att1_to_send["Content-Type"] = 'application/octet-stream'
        att1_to_send["Content-Disposition"] = f'attachment; filename={self.filename}'
        mail.attach(att1_to_send)

        try:
            service.sendmail(self.sender, self.recipient, mail.as_string())
            print("Successffully sent email")
        except SMTPAuthenticationError:
            print("The username and/or password you entered is incorrect")
        except (gaierror, ConnectionRefusedError):
            print('Failed to connect to the server. Bad connection settings?')
        except smtplib.SMTPServerDisconnected:
            print('Failed to connect to the server. Wrong user/password?')
        except smtplib.SMTPException as e:
            print('SMTP error occurred: ' + str(e))
        
        
    

# mail = Mail()
# mail.send()
