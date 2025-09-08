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

        return consumer


