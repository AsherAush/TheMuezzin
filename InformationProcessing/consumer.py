from kafka import KafkaConsumer
import os
from dotenv import load_dotenv
load_dotenv()

class KafkaSubscriber:
    def __init__(self, topic, bootstrap_servers):
        self.topic = topic
        self.bootstrap_servers = bootstrap_servers


    def subscribe(self):
        consumer = KafkaConsumer(
            self.topic , # השם של הנושא (topic)
            bootstrap_servers= self.bootstrap_servers

        )

        print(consumer.topics())
        for message in consumer:
            print(f"[KafkaSubscriber] Received message: {message.value.decode('utf-8')}")
            print(f"partition: {message.partition}, offset: {message.offset}")



a = KafkaSubscriber(os.getenv("TOPIC"), os.getenv("LOCAL_HOST"))
a.subscribe()