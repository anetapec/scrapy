from tricity.tricity.pipelines import MongoDBPipeline






class Attachment:
    
    def set_name_file(self, spider_mongo_collection):
        filename = str(spider_mongo_collection + self.set_scrapping_date())
        return filename
