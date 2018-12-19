import time
from RPi import GPIO

sensor_file = '/sys/bus/w1/devices/28-0516739dfeff/w1_slave'
GPIO.setmode(GPIO.BCM)

def read_temp_raw():
    with open(sensor_file, 'r') as f:
        lines = f.readlines()
    return lines


def read_temp():
    lines = read_temp_raw()
    equal_pos = lines[1].find('t=')
    if equal_pos != 1:
        return lines[1]

while 1:
    tempStr = read_temp()
    temp = float(tempStr[29:])/1000
    print("it's: " + str(temp)+ u'\u00b0' + "C")