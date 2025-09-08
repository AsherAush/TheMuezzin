import os
from dotenv import load_dotenv
from consumer import KafkaRetrieval
from Data_preparation import preparationData
from ElasticDal import Elastic
load_dotenv()

class main:
    def __init__(self):
        pass
        # A Kafka drawing
        self.retrieval = KafkaRetrieval(os.getenv("TOPIC"), os.getenv("LOCAL_HOST"))
        self.consumer = self.retrieval.retrieval()
        # Connect to ElasticSearch
        self.es = Elastic(os.getenv("ELASTICSEARCH_URL"), os.getenv("ELASTIC_INDEX"))
        self.es.create_index()


    def run(self):
        for message in self.consumer:
            data = message.value.decode("utf-8")
            prep = preparationData(data)
            prep.create_id()
            new_data = prep.data_to_elastic()
            print(len(new_data))
            self.es.insert_document(new_data)
            print(type(new_data))




if __name__ == "__main__":
    main().run()