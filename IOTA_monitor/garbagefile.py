from model.Logreader import LogReader
import urllib
from influxdb import InfluxDBClient
from time import time
import logging
from model.DatabaseManager import DatabaseManager

from model.FetchIotaTxs import FetchIotaTxs
import credentials
import threading



log = LogReader("updatedatabase.log")

mainNet = "https://nodes.thetangle.org:443"
seed_main_monitor = credentials.login["seed_main_monitor"]
target_address = credentials.login["target_address"]

dfa, dfb =log.preparedata_scatterplot()
print(dfa)








def test():
    dt_gettransfers, dur_gettransfers, samples_gettransfer, dt_txobject, dur_txobject,  samples_txobject = [], [], [],[],[],[]
    for line in LogReader("updatedatabase.log").readlog():
        try:
            levelname, u, m, s, method, value = line.split(":")
            date = str(u+m+s)
        except ValueError:
            pass

        try:
            if method.strip()=="get_transfers duration":
                dur_gettransfers.append(float(value.strip()))
                dt_gettransfers.append(date)
            elif method.strip() == "get_transfers # samples":
                samples_gettransfer.append(int(value.strip()))
            elif method.strip()=="find_transaction_objects duration":
                dur_txobject.append(float(value.strip()))
                dt_txobject.append(float(value.strip()))

            elif method.strip() == "find_transaction_objects # samples":
                samples_txobject.append(int(value.strip()))

        except UnboundLocalError:
            pass

    return dt_gettransfers, dur_gettransfers, samples_gettransfer, dt_gettransfers, dur_txobject,  samples_txobject


# a = "INFO 2019-01-22 02:25:56,981"
# print(len(a))

# dt_gettransfers, dur_gettransfers, samples_gettransfer, dt_gettransfers, dur_txobject,  samples_txobject = test()
# print(test())






# from time import time
# from flask import Flask, render_template
# from influxdb import InfluxDBClient
# from model.Logreader import LogReader
# from model.DatabaseManager import DatabaseManager
# import logging
# port = 8086
# host = 'localhost'
# dbname = "sensorvaluesiota"
#
# from datetime import datetime, timedelta
# def getSensorDataTimespan( timeSpan=1):
#     client = InfluxDBClient(host=host, port=port)
#     client.switch_database("sensorvaluesiota")
#     endTime = datetime.now()
#     startTime = endTime - timedelta(days=timeSpan)
#     str_st, str_end = "'" + str(startTime) + "'", "'" + str(
#         endTime) + "'"  # TODO fix safe params when influxdb is updated
#     temp, hum = client.query(('select * from temperature where time >= {} and time <= {} ').format(str_st, str_end)), client.query(
#         ('select * from humidity where time >= {} and time <= {} ').format(str_st, str_end))
#     temp_raw, hum_raw = temp.raw["series"][0]["values"], hum.raw["series"][0]["values"]
#     temp_points, hum_points = [l[3] for l in temp_raw], [l[1] for l in hum_raw]
#     labels = [l[0] for l in hum_raw]
#     print(temp_points)
#     print(labels)
#     return  temp_points, hum_points, labels
#
#
#
# start = time()
# # dbManager = DatabaseManager(host, port, dbname)
#
# getSensorDataTimespan(7)
# stop = time()
# print("duration connect to influxdb: " + str(stop - start))

