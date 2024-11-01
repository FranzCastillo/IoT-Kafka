import json

from confluent_kafka import Producer


class KafkaProducer:
    def __init__(self, address="lab9.alumchat.lol", port=9092, topic="21562"):
        self._bootstrap_servers = f"{address}:{port}"
        self._topic = topic
        self._producer = Producer({'bootstrap.servers': self._bootstrap_servers})

    def produce(self, data):
        self._producer.produce(self._topic, json.dumps(data).encode('utf-8'))
        self._producer.flush()
        print(f"Produced data to {self._topic}: {data}")

    def close(self):
        self._producer.flush()
