from elasticsearch import Elasticsearch


class Elastic:
    def __init__(self, host, index_name):
        self.client = Elasticsearch(hosts=host)
        self.index = index_name



    def create_index(self):
        if self.client.indices.exists(index=self.index):
            self.client.indices.delete(index=self.index)
        self.client.indices.create(index=self.index)

    def insert_document(self, doc):

        result = self.client.index(index=self.index, document=doc)
        return result["_id"]






