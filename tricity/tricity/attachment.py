from tricity.tricity.pipelines import MongoDBPipeline
from email.mime.text import MIMEText






class Add_attachment:
    
    def adding_attachment(self):
        att = MongoDBPipeline.set_name_file(MongoDBPipeline.spider_mongo_collection)    #name attachment
        attachment = MIMEText(open(att, 'rb').read(), 'base64', 'utf-8')
        



    
        
        
