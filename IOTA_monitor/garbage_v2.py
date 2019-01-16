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
query = 'select * from cpu_load_short;'


json_body = [
    {
        "measurement": "cpu_load_short",
        "tags": {
            "host": "server01",
            "region": "us-west"
        },
        "time": "2009-11-10T23:00:00Z",
        "fields": {
            "Float_value": 0.64,
            "Int_value": 3,
            "String_value": "Text",
            "Bool_value": True
        }
    }
]

print("Create database: " + dbname)
client.create_database(dbname)
client.switch_database(dbname)

print("Create a retention policy")
# client.create_retention_policy('awesome_policy', '3d', 3, default=True)

print("Switch user: " + dbuser)
client.switch_user(dbuser, dbuser_password)
print("Write points: {0}".format(json_body))
client.write_points(json_body)

print("Querying data: " + query)
result = client.query(query)

print("Result: {0}".format(result))

print("Switch user: " + user)
client.switch_user(user, password)

# print("Drop database: " + dbname)
# client.drop_database(dbname)

















