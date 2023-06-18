import pymongo
from tricity import settings
from datetime import datetime
import hashlib
from scrapy.exporters import CsvItemExporter
from scrapy.exceptions import DropItem
import os
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



class MongoDBPipeline:

    def set_hash_url(self,item):
        result_url = hashlib.md5(f"{item['price']}{item['url']}".encode('utf-8'))
        hash_value_url = result_url.hexdigest()
        return hash_value_url
    
    def set_hash_area(self,item):
        result_area = hashlib.md5(f"{item['price']}{item['area']}".encode('utf-8'))
        hash_value_area = result_area.hexdigest()
        return hash_value_area

    def set_scrapping_date(self):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return now
    
    def set_name_file(self, spider_mongo_collection):
        filename = str(spider_mongo_collection + self.set_scrapping_date())
        return filename
   
    def open_spider(self, spider):
        spider_mongo_collection = spider.custom_settings["collection"]
        self.scrapping_date = self.set_scrapping_date()
        self.client = pymongo.MongoClient(settings.mongodb_uri)
        db = self.client[settings.mongodb_db]
        self.collection = db[spider_mongo_collection]
        self.exporter = MongoDBPipeline.set_name_file(self, spider_mongo_collection)

    def close_spider(self, spider):
        self.client.close()
        file = open(self.set_name_file(spider_mongo_collection=spider.custom_settings["collection"]) + ".csv", 'w+b') 
        self.exporter = CsvItemExporter(file)
        self.exporter.start_exporting()
        self.exporter.finish_exporting()
        file.close()


        
        

    def process_item(self, item, spider):
        item['price_per_meter'] = (round(float(item['price']) / float(item['area']), 2))
        item['last_seen_date'] = self.scrapping_date
        item['hash'] = self.set_hash_url(item)
        item['hash_area'] = self.set_hash_area(item)
        filter_dict = {'hash': item['hash']}
        filter_dict_area = {'hash_area': item['hash_area']}
        if self.collection.count_documents((filter_dict), limit = 1) !=0 :
            new_value = { '$set': {'last_seen_date': item['last_seen_date']}}
            self.collection.update_one(filter_dict, new_value)
            raise DropItem("Duplicate item found: {}".format(item['scrapping_date']))
        if self.collection.count_documents((filter_dict_area), limit = 1) !=0 :
            new_value = { '$set': {'last_seen_date': item['last_seen_date']}}
            self.collection.update_one(filter_dict_area, new_value)
            raise DropItem("Duplicate item found: {}".format(item['scrapping_date']))
        else:
            item['scrapping_date'] = self.scrapping_date
            data = dict(item)
            self.collection.insert_one(data)
            
            self.exporter.export_item(item)

        return item
    

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

        att1 = name_att1.set_name_file(spider_mongo_collection='flats')
        #att1 = name_att1.open_spider(spider='flatsspider'(self.filename))
        att1 = MIMEText(open(name_att1, 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = f'attachment; filename={name_att1}'
        mail.attach(att1)

        try:
            service.sendmail(self.sender, self.recipient, mail.as_string())
            print("Successffully sent email")
        except  Exception as Error:
            print("Unable to send email")

# mail = Mail()
# mail.send()
    
    


        #ssl_connection = ssl.create_default_context()









        

        
