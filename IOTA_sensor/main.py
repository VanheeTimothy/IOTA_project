from time import time, sleep
import logging
from model.RGBmixer import RGBmixer
from model.TransferIotaTxs import TransferIotaTxs
from model import DHT11
from model import OneWire

logging.basicConfig(filename='logs/main.log', level=logging.INFO, format='%(levelname)s %(asctime)s %(message)s')

print("script running")

# one-wire params
sensor_file = '/sys/bus/w1/devices/28-0516739dfeff/w1_slave'
sensor = OneWire.OneWire(sensor_file)

# DHT11 params
humiditysensor = DHT11.DHT11(pin=14)

# LED RGB
RGBmixer = RGBmixer(16, 20, 21)

# mainNet params
mainNet = "https://nodes.thetangle.org:443"
seed_main_sensor = "MNYQVXGXWEWPTUJRPJIFVZUXDKJVWPNFQSQSHESZUQLZICBUABBRFSC9JBCAUCGSRZHX99LTBVRYUBBCV"
target_addres_monitor = "OOJTC99SSUPQIQCPVDUBXR9HM9FBZ9PXPNJAWUVRWHEPJWIGUFERAJYWOZCDXRSICYLVRBBYNEXBTEEVD"





_INTERVAL_MIN = 15
_WEIGHT = 14
_DEPTH = 3
manager = TransferIotaTxs(mainNet,seed_main_sensor)

def read_sensors():
    tempStr = str(sensor.read_temp())
    humidityStr = str(humiditysensor.read().humidity)
    while humidityStr == str(0):
        humidityStr = str(humiditysensor.read().humidity)
    return tempStr, humidityStr

def run():
    while 1:
        try:
            RGBmixer.green()
            start_1 = time()
            tempStr, humidityStr = read_sensors()
            stop_1 = time()
            logging.info("duration reading sensors: " + str(stop_1 - start_1))
            logging.info("reading temp: " + tempStr + "°C")
            logging.info("reading hummidity " + humidityStr + "%")


            logging.info("prepare transaction")
            start_2 = time()
            pt = manager.prepare_transaction(target_addres_monitor, tempStr, 'ONEWIREIOTA', 0)
            pt2 = manager.prepare_transaction(target_addres_monitor, humidityStr, 'DHTIOTA', 0)
            stop_2 = time()
            logging.info("duration prepare transactions: " + str(stop_2 - start_2))

            print("send transfer")
            logging.info("send transfer")
            start_3 = time()
            manager.send_transfers(_DEPTH, [pt, pt2], _WEIGHT)

            stop_3 = time()
            logging.info("Duration send transfer: " + str(stop_3 - start_3))
            print(("Duration send transfer: " + str(stop_3 - start_3)))
            logging.info("Duration of sequence: " + str(stop_3 - start_1))
            sleep_timer = 60 * _INTERVAL_MIN - (stop_3 - start_1)
            RGBmixer.blue()
            sleep(sleep_timer)

        except Exception as e:
            print("error")
            RGBmixer.red()
            logging.error(e)
            sleep(1)

        except KeyboardInterrupt as K:
            RGBmixer.yellow()
            sleep(0.5)
            RGBmixer.cleanUp()
            break





if __name__ == "__main__":
    run()
