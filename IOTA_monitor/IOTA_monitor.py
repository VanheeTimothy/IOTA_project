from time import time
from flask import Flask, render_template
from influxdb import InfluxDBClient
from model.Logreader import LogReader
import logging

logging.basicConfig(filename='logs/flask.log', level=logging.INFO, format='%(levelname)s %(asctime)s %(message)s')


start = time()
port = 8086
host = 'localhost'
dbname ="dbname"
client = InfluxDBClient(host=host, port=port)
client.switch_database(dbname)
stop = time()
logging.info("connected to influxdb using database: {}".format(dbname))
print("duration connect to influxdb: "+str(stop-start))




app = Flask(__name__)
@app.route('/')
def analytics():
    s = time()
    temp = client.query('SELECT "value" FROM temperature')
    humm = client.query('SELECT "value" FROM hummidity ')
    st = time()
    print("duration: " + str(st-s))
    logging.info("fetching temp and humm values from influxdb: {}s".format(st-s))
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
    s = time()
    temp, humm = client.query('SELECT * FROM temperature'), client.query('SELECT * FROM hummidity ')
    humm_raw, temp_raw = humm.raw["series"][0]["values"], temp.raw["series"][0]["values"]
    print(humm_raw)
    table_data = humm_raw + temp_raw #TODO sort values when None is
    st = time()
    logging.info("fetching transactions from influxdb: {}".format(str(st-s)))
    return render_template("Transactions.html",table_html=table_data)



@app.route('/logs')
def logs():
    s = time()
    readDbLog = LogReader("updatedatabase.log")
    readSensorLog = LogReader("sensor.log")
    dbLog = readDbLog.readlog()
    sensorLog = readSensorLog.readlog()
    st = time()
    logging.info("reading log files: {}".format(str(st-s)))

    return render_template('Logs.html', databaselog=dbLog, sensorlog=sensorLog ) #TODO add sensorlog=sensorLog



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
