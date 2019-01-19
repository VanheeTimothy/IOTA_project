from time import time

# import pandas as pd
from flask import Flask, render_template
from influxdb import InfluxDBClient
from model.Logreader import LogReader
from time import sleep
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# file_to_path = os.path.join(BASE_DIR, 'dummydata.txt')


# def readDummyData(file_to_path):
#     tempdata = []
#     fo = open(file_to_path)
#     c = 0
#     for line in fo:
#         line = line.rstrip("\n")
#         if float(line) >25:
#             c+=1
#         tempdata.append(float(line))
#     print(c)
#     return tempdata



# mainNet = "https://nodes.thetangle.org:443"
# mySeed_mainNet = "9EJ9QUK9PJYJGNSOZPZLB99VMBQQPMYYFIMFPOFJHWIIPLFAELRYSVZCEXZRGLJHGUKLFZORQWZAZYPK9"
# address_mainNet = "CPEIQD9UTUGPVBYRCUYYFISJARRBWNXBTANAINNYAVHJAOGTQWJGPORHXYXPVCJBH9XSVRCXVQHBFBNWD"
#
# devnet = "https://nodes.devnet.iota.org:443"
# address_devNet = b'TQJWJAD9MPSLOMUFZHMBKBYKPSSLLVILWAIEBKVIGOJDNE9DEFHB9KZROLRRQCOSEYVWEMO9TJURLZD9Y'
# mySeed_devNet  = "EXSZTFGBBNOPETQGSZEOP9DUBQEFH9XKSB9RTRR9RFCCPLEQZAGEJ9LLYWSUAWWMLURNJBFWOPVWTLBWP"
# test1 = FetchIotaTxs(devnet, mySeed_devNet, [address_devNet])


import datetime


start = time()
port = 8086
host = 'localhost'
client = InfluxDBClient(host=host, port=port)
client.switch_database("sensorvaluesiota")
stop = time()

print("duration connect to influxdb: "+str(stop-start))




app = Flask(__name__)
@app.route('/')
def analytics():
    temp_points, humm_points = [],[]
    s = time()
    temp = client.query('SELECT "value" FROM temperature')
    humm = client.query('SELECT "value" FROM hummidity ')
    st = time()
    # print(data)
    print("duration: " + str(st-s))
    temp_raw = temp.raw["series"][0]["values"]
    temp_points = [l[1] for l in temp_raw]
    humm_raw = humm.raw["series"][0]["values"]
    humm_points = [l[1] for l in humm_raw]





    return render_template('Analytics.html', tempdata=temp_points, hummdata=humm_points)


@app.route('/graphsdaily')
def graphsdaily():
    return render_template('GraphsDaily.html')


@app.route('/graphsweekly')
def grahpsweekly():
    return render_template('GraphsWeekly.html')

@app.route('/graphsmontly')
def graphsmonthly():
    return render_template('GraphsMonthly.html')



@app.route('/transactions')
def transactions():
    temp, humm = client.query('SELECT * FROM temperature'), client.query('SELECT * FROM hummidity ')
    humm_raw, temp_raw = humm.raw["series"][0]["values"], temp.raw["series"][0]["values"]
    print(humm_raw)
    table_data = humm_raw + temp_raw #TODO sort values when None is
    return render_template("Transactions.html",table_html=table_data)



@app.route('/logs')
def logs():
    readDbLog = LogReader("updatedatabase.log")
    readSensorLog = LogReader("sensor.log")
    dbLog = readDbLog.readlog()
    sensorLog = readSensorLog.readlog()

    return render_template('Logs.html', databaselog=dbLog, sensorlog=sensorLog ) #TODO add sensorlog=sensorLog



    # return app.response_class(generate(), mimetype='text/plain')




if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
