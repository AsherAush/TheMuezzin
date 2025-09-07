from Receiving_data import send_info_data
from publish_kafka import KafkaPublisher
import os
from dotenv import load_dotenv
import  json
load_dotenv()

class main:
    def __init__(self, path):
        self.path = path

    def run(self):
        files = send_info_data(self.path)
        data = files.get_data()
        data = json.loads(data)
        publisher = KafkaPublisher(bootstrap_servers=[os.getenv("LOCAL_HOST")], serializer="json")
        for item in data:
            publisher.publish(os.getenv("TOPIC"), item)
            print(item)
        publisher.close()









if __name__ == "__main__":
    main(os.getenv("PATH_FILE")).run()
