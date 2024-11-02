import json

from confluent_kafka import Consumer, KafkaException
from encoder_decoder import EncoderDecoder


class KafkaConsumer:
    def __init__(self, address="lab9.alumchat.lol", port=9092, topic="21562"):
        self._bootstrap_servers = f"{address}:{port}"
        self._topic = topic
        self._consumer = Consumer({
            'bootstrap.servers': self._bootstrap_servers,
            'group.id': '21552',
            'auto.offset.reset': 'earliest'
        })
        self._consumer.subscribe([self._topic])
        self.ed = EncoderDecoder()

    def consume(self):
        try:
            msg = self._consumer.poll(timeout=1.0)
            if msg is None:
                return None
            if msg.error():
                raise KafkaException(msg.error())
            
            raw_data = msg.value()
            data = self.ed.decode(raw_data)
            print(f"Consumed data from {self._topic}: {data}; raw: {msg.value()}")
            return data
        
        except KafkaException as e:
            print(f"Failed to consume data: {e}")
            return None

    def close(self):
        self._consumer.close()
