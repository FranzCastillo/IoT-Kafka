import time

import matplotlib.pyplot as plt

from consumer import KafkaConsumer


def main():
    consumer = KafkaConsumer()

    # Lists to store real-time data for plotting
    temperatures = []
    humidities = []
    timestamps = []

    plt.ion()  # Enable interactive mode
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

    try:
        while True:
            data = consumer.consume()
            if data is not None:
                # Extract data
                temperature = data["temperature"]
                humidity = data["humidity"]
                current_time = time.strftime("%H:%M:%S")

                # Append data for plotting
                temperatures.append(temperature)
                humidities.append(humidity)
                timestamps.append(current_time)

                # Limit the list size for real-time plotting
                if len(temperatures) > 20:
                    temperatures.pop(0)
                    humidities.pop(0)
                    timestamps.pop(0)

                # Clear axes and plot new data
                ax1.clear()
                ax2.clear()
                ax1.plot(timestamps, temperatures, label="Temperature (°C)")
                ax2.plot(timestamps, humidities, label="Humidity (%)")

                # Setting titles and labels
                ax1.set_title("Temperature over Time")
                ax1.set_ylabel("Temperature (°C)")
                ax2.set_title("Humidity over Time")
                ax2.set_ylabel("Humidity (%)")
                ax2.set_xlabel("Time")

                # Show legends
                ax1.legend(loc="upper right")
                ax2.legend(loc="upper right")

                plt.draw()  # Draw the updated plot
                plt.pause(1)  # Pause for brief update interval

            time.sleep(1)
    finally:
        consumer.close()
        plt.ioff()
        plt.show()


if __name__ == "__main__":
    main()
