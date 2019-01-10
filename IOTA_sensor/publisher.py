from iota.crypto.types import Seed  #importing PyOTA library to interact with
from iota.crypto.addresses import AddressGenerator
import iota
import datetime
from pprint import pprint
from time import time
from RPi import GPIO

from model import OneWire
sensor_file = '/sys/bus/w1/devices/28-0516739dfeff/w1_slave'
GPIO.setmode(GPIO.BCM)
sensor = OneWire.OneWire(sensor_file)


devnet = "https://nodes.devnet.iota.org:443"
mySeed_devnet = "SAEWHQJPUIGDKLB9FQ9XTNYZTWRRYVLZAFMGRYYNAFIEMUWNUADVTZTMLYQCLPSJVKJHZTSMYZWWIFXSW"
targetAddress_devnet = b'TQJWJAD9MPSLOMUFZHMBKBYKPSSLLVILWAIEBKVIGOJDNE9DEFHB9KZROLRRQCOSEYVWEMO9TJURLZD9Y'

mainNet = "https://nodes.thetangle.org:443"
mySeed_mainNet = "QG9PRLCNUGJRE9XLJUXJLP9ZQKBSCQXCDMWHWZWYSVMYFXYWDSJFTTUMVMFHKUSJNJATWUFVIKUPVPVIN"
targetAddress_mainNet = "JMZQEQFYKVLZXHXUQLOYQZWHWI9VGTLR9LJVYCONEDLZHBBUVFZHDKR9WHN9LNDGZMXYKQFNJGHKROLLA"


api = iota.Iota(devnet,seed=mySeed_devnet )


def prepare_transaction(targetAddress, msg,tag, value):
    # preparing a transaction
    pt = iota.ProposedTransaction(address=iota.Address(targetAddress),
                                  message=iota.TryteString.from_unicode(str(msg)),
                                  tag=iota.Tag(bytes(tag, 'utf8')),
                                  value=value)
    return pt



start = time()
# STEP1: prepare transaction(s)
# pt = prepare_transaction(targetAddress_devnet, '18.06','RASPBERRYHOWESTIOTA',0)

while 1:
    tempStr = str(sensor.read_temp())
    print("reading temp: ")
    print(tempStr)
    print("prepare transaction:")
    pt = prepare_transaction(targetAddress_devnet, tempStr, 'RASPBERRYHOWESTIOTA', 0)
    print("send transfer")
    FinalBundle = api.send_transfer(depth=3,
                                    transfers=[pt],
                                    min_weight_magnitude=9)['bundle']  # it returns a dictionary with a bundle object





