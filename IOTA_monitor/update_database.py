import logging
from time import time
from influxdb import InfluxDBClient
from model.FetchIotaTxs import FetchIotaTxs
import credentials
logging.basicConfig(filename='logs/updatedatabase.log', level=logging.INFO, format='%(levelname)s:%(asctime)s:%(message)s')

mainNet = "https://nodes.thetangle.org:443"
seed_main_monitor = credentials.login["seed_main_monitor"]
target_address = credentials.login["target_address"]





# ## testing

try:
    start = time()

    fetcher = FetchIotaTxs(mainNet, seed_main_monitor, [target_address])
    temp_data, hum_data = fetcher.get_querry_list(methode=1)
    stop = time()
    print("duration= " + str(stop - start))
    logging.info("get_transfers duration: " + str(round(stop - start, 3)))
    logging.info("get_transfers # samples: " + str(len(temp_data) + len(hum_data)))
except Exception as e:
    logging.error("error invoked by method: get_transfers\n{}".format(e))



## real values

try:
    start = time()
    fetcher = FetchIotaTxs(mainNet, seed_main_monitor, [target_address])
    temp_data, hum_data = fetcher.get_querry_list(methode=0)
    stop = time()
    print("duration= " + str(stop - start))
    logging.info("find_transaction_objects duration: " + str(round(stop - start, 3)))
    logging.info("find_transaction_objects # samples: " + str(len(temp_data) + len(hum_data)))
except Exception as e:
    logging.error("error invoked by method: find_txobject")
    logging.error(e)




s = time()
temp_list = sorted(temp_data, key=lambda k: k['time'])
hum_list = sorted(hum_data, key=lambda k: k['time'])
st = time()
print(temp_list)
print(hum_list)
print("duration sorting " +str(st-s))
logging.info("duration sorting values: " +str(round(st-s,6))+" s")


# influxdb
print("influx db:")
host = 'localhost'
port = 8086
client = InfluxDBClient(host=host,port=port)
db_name = "iotatransactions"
db_found = False
dblist = client.get_list_database()
for db in dblist:
        if db['name'] == db_name:
            db_found = True
        if not(db_found):
            client.create_database(db_name)


try:
    print("write data into db")
    logging.info("write data into db")
    client.switch_database(db_name)
    client.write_points(temp_data)
    client.write_points(hum_list)
except Exception as e:
    logging.error(e)


