import random


class Sensor:
    def __init__(self, lowest_temperature=0.0, highest_temperature=110.0, lowest_humidity=0.0, highest_humidity=100.0):
        self._seed = 2024

        self._lowest_temperature = lowest_temperature
        self._highest_temperature = highest_temperature
        self._mean_temperature = 55
        self._std_temperature = 20

        self._lowest_humidity = lowest_humidity
        self._highest_humidity = highest_humidity
        self._mean_humidity = 55
        self._std_humidity = 20

        self._wind_directions = ['N', 'NO', 'O', 'SO', 'S', 'SE', 'E', 'NE']

        random.seed(self._seed)

    def get_temperature(self):
        temp = round(random.normalvariate(self._mean_temperature, self._std_temperature), 2)
        return max(
            self._lowest_temperature,
            min(
                self._highest_temperature,
                temp
            )
        )

    def get_humidity(self):
        humidity = round(random.normalvariate(self._mean_humidity, self._std_humidity), 2)
        return max(
            self._lowest_humidity,
            min(
                self._highest_humidity,
                humidity
            )
        )

    def get_wind_direction(self):
        return random.choice(self._wind_directions)

    def get_json(self):
        return {
            "temperature": self.get_temperature(),
            "humidity": self.get_humidity(),
            "wind_direction": self.get_wind_direction()
        }
