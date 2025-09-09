from elasticsearch import Elasticsearch
from LoggerFile import Logger

logger = Logger.get_logger()


class Send_elastic:
    def __init__(self, host, index_name):
        try:
            self.client = Elasticsearch(host)
            self.index = index_name
            logger.info("Connected to Elasticsearch")
        except Exception as e:
            logger.error(f"Error connecting to Elasticsearch:")
            print(f"Error connecting  Elasticsearch: {e}")




    def update_document(self, doc_id, update_fields):

        try:

            self.client.update(index=self.index, id=doc_id, body={"doc" : {"text": update_fields}})

            logger.info(f"Document updated with ID: {doc_id}")
            return True
        except Exception as e:
            logger.error(f"Error updating document: {e}")
            return False