from time import time
from flask import Flask, render_template
from influxdb import InfluxDBClient
from model.Logreader import LogReader
from model.DatabaseManager import DatabaseManager
import logging

logging.basicConfig(filename='logs/flask.log', level=logging.INFO, format='%(levelname)s %(asctime)s %(message)s')

port = 8086
host = 'localhost'
dbname = "sensorvaluesiota"



try:
    start = time()
    dbManager = DatabaseManager(host, port, dbname)
    stop = time()
    logging.info("connected to influxdb using database: {}".format(dbname))
    print("duration connect to influxdb: "+str(stop-start))
except Exception as e:
    logging.error(e)


app = Flask(__name__)
@app.route('/')
def analytics():
    try:
        s = time()
        temp_points, humm_points, labels = dbManager.getSensorData()
        st = time()
        logging.info("fetching temp and humm values from influxdb: {}s".format(round(st-s,3)))
    except Exception as e:
        logging.error(e)

    return render_template('Analytics.html', tempdata=temp_points, hummdata=humm_points, labels=labels)


@app.route('/graphsdaily')
def graphsdaily():


    return render_template('GraphsDaily.html')


@app.route('/graphsweekly')
def grahpsweekly():
    return render_template('GraphsWeekly.html')

@app.route('/graphsmontly')
def graphsmonthly():
    return render_template('GraphsMonthly.html')

@app.route('/insightslog')
def insightslog():
    try:
        readDbLog = LogReader("updatedatabase.log")
        duration, samples = readDbLog.getDatapointslog()
    except Exception as e:
        logging.error(e)

    return render_template('InsightsLog.html',duration=duration, samples=samples)





@app.route('/transactions')
def transactions():
    try:
        s = time()
        txs = dbManager.getTransactions()
        st = time()
        logging.info("fetching transactions from influxdb: {}".format(str(round(st - s, 3))))
    except Exception as e:
        logging.error(e)

    return render_template("Transactions.html",table_html=txs)



@app.route('/logs')
def logs():
    try:
        s = time()
        readDbLog, readSensorLog, readFlaskLog = LogReader("updatedatabase.log"), LogReader("sensor.log"), LogReader("flask.log")
        dbLog, sensorLog, flaskLog  = readDbLog.readlog(), readSensorLog.readlog(), readFlaskLog.readlog()
        st = time()
        logging.info("reading log files: {}".format(str(round(st-s,3))))

    except Exception as e:
        logging.error(e)

    return render_template('Logs.html', databaselog=dbLog, sensorlog=sensorLog, flasklog=flaskLog ) #TODO add sensorlog=sensorLog



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
