import board
from adafruit_onewire.bus import OneWireBus
from adafruit_ds18x20 import DS18X20


class Sensor:
    ''' Sensor class which contains all the code for interacting with sensors aboard the weather station '''

    # variables
    water_temp_sensor = None
    ow_bus = None
    ow_devices = None

    # initialize sensor variables
    def __init__(self) -> None:
        self.ow_bus = OneWireBus(board.GP22)
        self.ow_devices = self.ow_bus.scan()
        self.water_temp_sensor = DS18X20(self.ow_bus, self.ow_devices[0])
    
    # returns dictionary of all sensor values
    def get_dict(self) -> dict:
        return {'water temp': self.get_water_temperature()}

    # get temperature from ds18x20 tied to GP22 in euro units
    def get_water_temperature(self) -> float:
        return round(self.water_temp_sensor.temperature, 2)
