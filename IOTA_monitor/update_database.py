import logging
from time import time

from influxdb import InfluxDBClient

from model.FetchIotaTxs import FetchIotaTxs

logging.basicConfig(filename='logs/updatedatabase.log', level=logging.INFO, format='%(levelname)s %(asctime)s %(message)s')



mainNet = "https://nodes.thetangle.org:443"
seed_main_monitor = "CUTFTOMSWETGHFQQGLXOXLDSLRTQQZUPI9QJUHESFLNZGSUOLABWXIIYOGMJJNYBVBIKNSCWZZRITUKLV"
target_addres = "9PGAPJOUSVS9TVTLVYNMWEJIMBQVKAYKF9CMGVN9SINNLUDJFVDJCGN9JTJ9SCW9HWMCRCKHCSJPSPDZD"





start = time()
test1 = FetchIotaTxs(mainNet, seed_main_monitor, [target_addres])
temp_data, humm_data = test1.get_querry_list()
stop  = time()
print("duration= "+str(stop-start))
logging.info("fetch iota's duration: "+str(stop-start)+" s")
logging.info("total length samples "+str(len(temp_data)+len(humm_data)))


s = time()
temp_list = sorted(temp_data, key=lambda k: k['time'])
humm_list = sorted(humm_data, key=lambda k: k['time'])
st = time()
print(temp_list)
print(humm_list)
print("duration sorting " +str(st-s))
logging.info("duration sorting values: " +str(st-s)+" s")


# influxdb
print("influx db:")
host = 'localhost'
port = 8086
client = InfluxDBClient(host=host,port=port)
client.switch_database("sensorvaluesiota")
print("write data into db")
logging.info("write data into db")

try:
    client.write_points(temp_data)
    client.write_points(humm_list)
except Exception as e:
    print("#####################################")
    print(e)
    logging.error(e)

# client.write_points(temp_data, time_precision=None, database=None, retention_policy=None, tags=None, batch_size=None, protocol=u'json')
print("fetch data from db")
s = time()
data = client.query("SELECT * FROM temperature")
# client.query('SELECT "value" FROM "sensorvaluesiota"."autogen"."temperatures" WHERE time > now() - 4d GROUP BY "time"')
st = time()
print(data)
print("len list temp_data "+ str(len(temp_data)))



print("duration: "+str(st-s))