from Receiving_data import send_info_data
from kafka import KafkaProducer
import json



class KafkaPublisher:
    def __init__(self, bootstrap_servers: list[str], serializer: str = "json"):
        self.bootstrap_servers = bootstrap_servers
        self.serializer = lambda v: json.dumps(v).encode("utf-8")
        self.producer = KafkaProducer(
            bootstrap_servers=self.bootstrap_servers,
            value_serializer=self.serializer,
        )

    def publish(self, topic: str, message):
        future = self.producer.send(
            topic,
            value=message
        )
        record_metadata = future.get(timeout=10)
        print(f"[KafkaPublisher] Sent to {record_metadata.topic}, "
              f"partition {record_metadata.partition}, offset {record_metadata.offset}")
    def close(self):
        self.producer.flush()
        self.producer.close()
        print("[KafkaPublisher] Connection closed.")


