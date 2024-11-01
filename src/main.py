from sensor import Sensor

SERVER_ADDRESS = "lab9.alumchat.lol"
SERVER_IP = "164.92.76.15"
SERVER_PORT = 9092


def main():
    sensor = Sensor()

    for i in range(5):
        print(sensor.get_json())


if __name__ == "__main__":
    main()
