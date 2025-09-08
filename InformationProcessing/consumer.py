from kafka import KafkaConsumer
import os
from dotenv import load_dotenv
load_dotenv()
from Logger_file import Logger

logger = Logger.get_logger()

class KafkaRetrieval:
    def __init__(self, topic, bootstrap_servers):
        try:
            self.topic = topic
            self.bootstrap_servers = bootstrap_servers
            logger.info("The muazin started")
        except Exception as e:
            print(f"Error KafkaRetrieval: {e}")
            logger.error(f"Error connecting to KafkaRetrival:")


    def retrieval(self):
        consumer = KafkaConsumer(
            self.topic ,
            bootstrap_servers= self.bootstrap_servers

        )

        return consumer


