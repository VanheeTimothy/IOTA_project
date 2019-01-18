from time import time
from influxdb import InfluxDBClient
import html.parser as htmlparser
import html
parser = htmlparser.HTMLParser()





mainNet = "https://nodes.thetangle.org:443"
mySeed_mainNet = "9EJ9QUK9PJYJGNSOZPZLB99VMBQQPMYYFIMFPOFJHWIIPLFAELRYSVZCEXZRGLJHGUKLFZORQWZAZYPK9"
address_mainNet = "CPEIQD9UTUGPVBYRCUYYFISJARRBWNXBTANAINNYAVHJAOGTQWJGPORHXYXPVCJBH9XSVRCXVQHBFBNWD"

devnet = "https://nodes.devnet.iota.org:443"
address_devNet = b'HIWQVEVOEVGQQVVZIHNVAKVYCPPGYOLQBEQBAWDYIUJOXJVFJEKOHYNMRZELUXDTXFPDFUCKGDBDQOVEZ'
mySeed_devNet  = "EXSZTFGBBNOPETQGSZEOP9DUBQEFH9XKSB9RTRR9RFCCPLEQZAGEJ9LLYWSUAWWMLURNJBFWOPVWTLBWP"

# influxdb
print("influx db:")
host = 'localhost'
port = 8086
client = InfluxDBClient(host=host,port=port)
user = 'root'
password = 'root'
dbname = 'example'
dbuser = 'smly'
dbuser_password = 'my_secret_password'


client.switch_database("sensorvaluesiota")


# client.write_points(temp_data, time_precision=None, database=None, retention_policy=None, tags=None, batch_size=None, protocol=u'json')
print("fetch data from db")
s = time()
data = client.query('SELECT * FROM temperature')
# client.query('SELECT "value" FROM "sensorvaluesiota"."autogen"."temperatures" WHERE time > now() - 4d GROUP BY "time"')
st = time()
print(data.raw)

dd = [x for x in data.raw["series"]]
print(dd)

print("---------------------")



print(data.raw["series"][0]["values"])

print("duration: "+str(st-s))















