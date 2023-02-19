

from itemadapter import ItemAdapter


class TricityPipeline:
    def process_item(self, item, spider):

        print(f" Pipeline:" + item['price_per_meter'][0])
        return item
