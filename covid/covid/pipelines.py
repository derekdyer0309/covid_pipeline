# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
import logging


class MongodbPipeline:
    collection_name = 'covid_data'

    def open_spider(self, spider):
        self.client = pymongo.MongoClient("mongodb+srv://derek:BRSiYvsx46UTlEFM@covid.cqshl.mongodb.net/<dbname>?retryWrites=true&w=majority")
        self.db = self.client['covid']

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert(item)
        return item


class TotalsPipeline:
    collection_name = 'covid_totals'

    def open_spider(self,spider):
        self.client = pymongo.MongoClient("mongodb+srv://derek:BRSiYvsx46UTlEFM@covid.cqshl.mongodb.net/<dbname>?retryWrites=true&w=majority")
        self.db = self.client['covid']

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert(item)
        return item 
