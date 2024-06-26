import board
import adafruit_dht
from analogio import AnalogIn


class Sensor:
    """Sensor class which contains all the code for interacting with sensors aboard the weather station"""

    # variables
    dht22 = None
    ws_pin = None

    # initialize sensor variables
    def __init__(self) -> None:
        # DHT 22
        self.dht22 = adafruit_dht.DHT22(board.GP16)

        # Water Sensor analog in pin to get voltage

        self.ws_pin = AnalogIn(board.GP26)

    # returns dictionary of all sensor values
    def get_dict(self) -> dict:
        return {
            "temp": self.get_temperature(),
            "humidity": self.get_humidity(),
            "raining": self.get_water_sensor(),
        }

    # get temperature from DHT22 tied to GP16 in freedom units 🦅🦅🦅
    def get_temperature(self) -> float:
        return self.dht22.temperature * (9 / 5) + 32

    # get humidity from DHT22 tied to GP16
    def get_humidity(self) -> float:
        return self.dht22.humidity

    # get water sensor state
    def get_water_sensor(self) -> bool:
        # if the value is greater than 1000 it's probably raining and this will return true if
        # this is the case.

        return (lambda: True if self.ws_pin.value > 1000 else False)()
