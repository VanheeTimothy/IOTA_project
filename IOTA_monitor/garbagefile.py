from model.Logreader import LogReader
import urllib
from influxdb import InfluxDBClient
from time import time
import logging
from model.DatabaseManager import DatabaseManager
port = 8086
host = 'localhost'
dbname = "sensorvaluesiota"




start = time()
dbManager = DatabaseManager(host, port, dbname)
stop = time()
logging.info("connected to influxdb using database: {}".format(dbname))
print("duration connect to influxdb: "+str(stop-start))
dd = dbManager.getSensorDatatest()
print(dd)


