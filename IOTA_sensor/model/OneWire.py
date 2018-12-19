import time
from RPi import GPIO

class OneWire:

    def __init__(self, sensorFile):
        self.senorfile = sensorFile

    def read_temp(self):
        lines = self.read_temp_raw()
        equal_pos = lines[1].find('t=')
        if equal_pos != 1:
            return float(lines[1][29:])/1000

    def read_temp_raw(self):
        with open(self.senorfile, 'r') as f:
            lines = f.readlines()
        return lines



