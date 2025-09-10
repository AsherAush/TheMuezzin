import os
from dotenv import load_dotenv
from consumer import KafkaRetrieval
from Data_preparation import preparationData
from ElasticDal import Elastic
from MongoDal import Mongo
load_dotenv()

class main:
    def __init__(self):
        # A Kafka drawing
        self.retrieval = KafkaRetrieval(os.getenv("TOPIC"), os.getenv("LOCAL_HOST"))
        self.consumer = self.retrieval.retrieval()
        # Connect to ElasticSearch
        self.es = Elastic(os.getenv("ELASTICSEARCH_URL"), os.getenv("ELASTIC_INDEX"))
        self.es.create_index()
        # Connect to MongoDB
        self.mongo = Mongo(os.getenv("MONGO_URL"), os.getenv("DB_NAME"))



    def run(self):

        for message in self.consumer:
            # rerurn json data
            data = message.value.decode("utf-8")
            prep = preparationData(data)
            prep.create_id()

            elastic_db = prep.data_to_elastic()
            self.es.insert_document(elastic_db)

            mondo_db = prep.data_to_mongo()
            self.mongo.upload_wav(mondo_db["full_path"], mondo_db["_id"])







if __name__ == "__main__":
    main().run()