from Receiving_data import send_info_data
from publish_kafka import KafkaPublisher
import  json

class main:
    def __init__(self, path):
        self.path = path

    def run(self):
        files = send_info_data(self.path)
        data = files.get_data()
        data = json.loads(data)
        publisher = KafkaPublisher(bootstrap_servers=["localhost:9092"], serializer="json")
        for item in data:
            publisher.publish("File_data", item)
            print(item)
        publisher.close()









if __name__ == "__main__":
    main("C:/podcasts").run()
