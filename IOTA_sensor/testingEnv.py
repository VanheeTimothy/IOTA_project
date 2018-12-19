from RPi import GPIO
from iota.crypto.types import Seed  #importing PyOTA library to interact with
from iota.crypto.addresses import AddressGenerator
import iota
import datetime
from pprint import pprint
from time import time
import sys
sys.path.append('/home/pi/IOTA_sensor/model')
import OneWire
from time import sleep
targetAddress_mainNet = "CPEIQD9UTUGPVBYRCUYYFISJARRBWNXBTANAINNYAVHJAOGTQWJGPORHXYXPVCJBH9XSVRCXVQHBFBNWD"
mySeed_mainNet = "QG9PRLCNUGJRE9XLJUXJLP9ZQKBSCQXCDMWHWZWYSVMYFXYWDSJFTTUMVMFHKUSJNJATWUFVIKUPVPVIN"
mainNet = "https://nodes.thetangle.org:443"


sensor_file = '/sys/bus/w1/devices/28-0516739dfeff/w1_slave'
GPIO.setmode(GPIO.BCM)
sensor = OneWire.OneWire(sensor_file)
nowIs = datetime.datetime.now()
def prepare_transaction(targetAddress, msg,tag, value):
    # preparing a transaction
    pt = iota.ProposedTransaction(address=iota.Address(targetAddress),
                                  message=iota.TryteString.from_unicode(str(msg)),
                                  tag=iota.Tag(bytes(tag, 'utf8')),
                                  value=value)
    return pt

api = iota.Iota(mainNet,seed=mySeed_mainNet )
while 1:
    start = time()
    tempStr = str(sensor.read_temp())
    print("reading temp: ")
    print(tempStr)
    print("prepare transaction")
    pt = prepare_transaction(targetAddress_mainNet, tempStr, 'ONEWIRESENSORIOTA', 0)
    print("send transfer")
    FinalBundle = api.send_transfer(depth=3, transfers=[pt], min_weight_magnitude=14)["bundle"]
    stop = time()
    print("duration: "+str(stop-start))

    # temp = float(tempStr[29:])/1000
    # print("it's: " + str(temp)+ u'\u00b0' + "C")



