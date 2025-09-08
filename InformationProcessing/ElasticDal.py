from elasticsearch import Elasticsearch
from Logger_file import Logger

logger = Logger.get_logger()


class Elastic:
    def __init__(self, host, index_name):
        try:
            self.client = Elasticsearch(hosts=host)
            self.index = index_name
            logger.info("The muazin started")
        except Exception as e:
            logger.error(f"Error connecting to Elasticsearch:")
            print(f"Error connecting  Elasticsearch: {e}")






    def create_index(self):
        if self.client.indices.exists(index=self.index):
            self.client.indices.delete(index=self.index)
        self.client.indices.create(index=self.index)

    def insert_document(self, doc):

        result = self.client.index(index=self.index, document=doc)
        return result["_id"]






