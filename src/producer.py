import json

from confluent_kafka import Producer
from encoder_decoder import EncoderDecoder


class KafkaProducer:
    def __init__(self, address="lab9.alumchat.lol", port=9092, topic="21562"):
        self._bootstrap_servers = f"{address}:{port}"
        self._topic = topic
        self._producer = Producer({'bootstrap.servers': self._bootstrap_servers})
        self.ed = EncoderDecoder()

    def produce(self, data):
        encoded_data = self.ed.encode(data)
        encoded_data_len = self.ed.sizeOf(data)
        self._producer.produce(self._topic, encoded_data)
        self._producer.flush()
        print(f"Produced data to {self._topic}: {data}; encoded: {encoded_data}; size: {encoded_data_len} bytes")

    def close(self):
        self._producer.flush()
