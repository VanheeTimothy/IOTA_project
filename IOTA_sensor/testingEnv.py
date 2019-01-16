
from model import DHT11
humiditysensor = DHT11.DHT11(pin=14)

humidityWaarde = humiditysensor.read().humidity
print(humidityWaarde)
if humidityWaarde != 0 and humidityWaarde != None:
    print("humidty on")