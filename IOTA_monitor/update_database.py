from FetchIotaTxs import FetchIotaTxs
from influxdb import InfluxDBClient
from time import time
import re
from pprint import pprint
mainNet = "https://nodes.thetangle.org:443"
mySeed_mainNet = "9EJ9QUK9PJYJGNSOZPZLB99VMBQQPMYYFIMFPOFJHWIIPLFAELRYSVZCEXZRGLJHGUKLFZORQWZAZYPK9"
address_mainNet = "CPEIQD9UTUGPVBYRCUYYFISJARRBWNXBTANAINNYAVHJAOGTQWJGPORHXYXPVCJBH9XSVRCXVQHBFBNWD"

devnet = "https://nodes.devnet.iota.org:443"
address_devNet = b'HIWQVEVOEVGQQVVZIHNVAKVYCPPGYOLQBEQBAWDYIUJOXJVFJEKOHYNMRZELUXDTXFPDFUCKGDBDQOVEZ'
mySeed_devNet  = "EXSZTFGBBNOPETQGSZEOP9DUBQEFH9XKSB9RTRR9RFCCPLEQZAGEJ9LLYWSUAWWMLURNJBFWOPVWTLBWP"



start = time()
test1 = FetchIotaTxs(devnet, mySeed_devNet, [address_devNet])
temp_data, humm_data = test1.get_querry_list()
stop  = time()
print("duration= "+str(stop-start))

s = time()
temp_list = sorted(temp_data, key=lambda k: k['time'])
humm_list = sorted(humm_data, key=lambda k: k['time'])
st = time()
print(temp_list)
print(humm_list)
print("duration sorting " +str(st-s))

# influxdb
print("influx db:")
host = 'localhost'
port = 8086
client = InfluxDBClient(host=host,port=port)
client.switch_database("sensorvaluesiota")
print("write data into db")
try:
    client.write_points(temp_data)
    client.write_points(humm_list)
except Exception as e:
    print("#####################################")
    print(e)

# client.write_points(temp_data, time_precision=None, database=None, retention_policy=None, tags=None, batch_size=None, protocol=u'json')
print("fetch data from db")
s = time()
data = client.query("SELECT * FROM temperature")
# client.query('SELECT "value" FROM "sensorvaluesiota"."autogen"."temperatures" WHERE time > now() - 4d GROUP BY "time"')
st = time()
print(data)

print("duration: "+str(st-s))