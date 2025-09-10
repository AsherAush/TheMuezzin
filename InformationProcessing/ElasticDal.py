from elasticsearch import Elasticsearch
from LoggerFile import Logger

logger = Logger.get_logger()


class Elastic:
    def __init__(self, host, index_name):
        try:
            self.client = Elasticsearch(hosts=host)
            self.index = index_name
            logger.info("Connected to Elasticsearch")
        except Exception as e:
            logger.error(f"Error connecting to Elasticsearch:")
            print(f"Error connecting  Elasticsearch: {e}")






    def create_index(self):
        if self.client.indices.exists(index=self.index):
            self.client.indices.delete(index=self.index)
        self.client.indices.create(index=self.index)

    def insert_document(self, doc):
        try:
            result = self.client.index(index=self.index, id= doc["id"], document=doc)
            logger.info(f"Document inserted with ID: {result['_id']}")

        except Exception as e:
            logger.error(f"Error inserting document: {e}")
            return None






