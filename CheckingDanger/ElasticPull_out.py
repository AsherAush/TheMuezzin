from elasticsearch import Elasticsearch
from DecodingText import Decoding
import os
from dotenv import load_dotenv
load_dotenv()


class Pull_elastic:
    def __init__(self, host, index ):
        self.es = Elasticsearch(host)
        self.index = index

    def pull(self):
        result = {}
        search_query = {"size" : 10000,
            "query": {
                "match_all": {}

            }
        }

        response = self.es.search(index=self.index, body=search_query)

        hits = response["hits"]["hits"]

        for hit in hits:
            document_id = hit["_id"]
            field_value = hit["_source"].get("text")
            result[document_id] = field_value


            # print(f"Document ID: {document_id}, Field Value: {field_value}")
            # print(document_id)
            # print(field_value)
        return result


#
# a = Pull_elastic(os.getenv("ELASTICSEARCH_URL"), os.getenv("ELASTIC_INDEX"))
# b= a.pull()
# c = Decoding()
# test = c.decodingHostile()
# for key, value in b.items():
#     print(key)
#     for word in test.lower().split(","):
#         if word in value.lower():
#             print(word)
