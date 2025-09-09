from Receiving_data import send_info_data
from kafka import KafkaProducer
import json
from dotenv import load_dotenv
load_dotenv()
import LoggerFile
logger = LoggerFile.Logger.get_logger()



class KafkaPublisher:
    def __init__(self, bootstrap_servers: list[str], serializer: str = "json"):
        try:
            self.bootstrap_servers = bootstrap_servers
            self.serializer = lambda v: json.dumps(v).encode("utf-8")
            logger.info("Connected to Kafka Publisher")
            self.producer = KafkaProducer(
                bootstrap_servers=self.bootstrap_servers,
                value_serializer=self.serializer,
            )

        except Exception as e:
            logger.error(f"Error connecting to KafkaPublisher: {e}")
            print(f"Error KafkaPublisher: {e}")


    def publish(self, topic: str, message):
        future = self.producer.send(
            topic,
            value=message
        )
        record_metadata = future.get(timeout=1)
        print(f"[KafkaPublisher] Sent to {record_metadata.topic}, "
              f"partition {record_metadata.partition}, offset {record_metadata.offset}")
    def close(self):
        self.producer.flush()
        self.producer.close()
        print("[KafkaPublisher] Connection closed.")


