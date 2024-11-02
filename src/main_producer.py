import time

from producer import KafkaProducer
from sensor import Sensor


def main():
    sensor = Sensor()
    kafka_producer = KafkaProducer()

    try:
        # Send data every 30 seconds
        while True:
            data = sensor.get_json()
            kafka_producer.produce(data)

            # Sleep for 30 seconds
            time.sleep(30)
    finally:
        kafka_producer.close()


if __name__ == "__main__":
    main()
