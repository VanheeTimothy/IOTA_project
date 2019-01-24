from time import time
from flask import Flask, render_template
from influxdb import InfluxDBClient
from model.Logreader import LogReader
from model.DatabaseManager import DatabaseManager
import logging

logging.basicConfig(filename='logs/flask.log', level=logging.INFO, format='%(levelname)s %(asctime)s %(message)s')

port = 8086
host = 'localhost'
dbname = "iotatransactions"

try:
    start = time()
    dbManager = DatabaseManager(host, port, dbname)
    stop = time()
    logging.info("connected to influxdb using database: {}".format(dbname))
    print("duration connect to influxdb: " + str(stop - start))
except Exception as e:
    logging.error(e)

app = Flask(__name__)


# @app.route('/')
# def analytics():
#     try:
#         s = time()
#         temp_points, humm_points, labels = dbManager.getAllSensorData()
#         st = time()
#         logging.info("fetching temp and humm values from influxdb: {}s".format(round(st - s, 3)))
#     except Exception as e:
#         logging.error(e)
#
#     return render_template('Analytics.html', tempdata=temp_points, hummdata=humm_points, labels=labels)


@app.route('/')
def graphsdaily():
    try:

        s = time()
        temp_points, humm_points, labels = dbManager.getAllSensorData()
        logging.info("{}".format(str(temp_points)))

        st = time()
        logging.info("fetching temp and humm values from influxdb: {}s".format(round(st - s, 3)))
    except Exception as e:
        logging.error(e)

    return render_template('GraphsDaily.html', tempdata=temp_points, hummdata=humm_points, labels=labels)


@app.route('/graphsweekly')
def grahpsweekly():
    try:
        s = time()
        temp_points, humm_points, labels = dbManager.getSensorDataTimespan(7)
        st = time()
        logging.info("fetching temp and humm values from influxdb: {}s".format(round(st - s, 3)))
    except Exception as e:
        logging.error(e)

    return render_template('GraphsDaily.html', tempdata=temp_points, hummdata=humm_points, labels=labels)


@app.route('/graphsmontly')
def graphsmonthly():
    try:
        s = time()
        temp_points, humm_points, labels = dbManager.getSensorDataTimespan(31)
        st = time()
        logging.info("fetching temp and humm values from influxdb: {}s".format(round(st - s, 3)))

    except Exception as e:
        logging.error(e)


    return render_template('GraphsDaily.html', tempdata=temp_points, hummdata=humm_points, labels=labels)


@app.route('/insightslog')
def insightslog():
    readDbLog = LogReader("updatedatabase.log")
    try:

        dt_gettransfers, dur_gettransfers, samples_gettransfer, dt_txobject, dur_txobject, samples_txobject = readDbLog.getDatapointsLog()
        logging.info(len(dt_gettransfers))
        logging.info(len(dur_gettransfers))
        logging.info(len((samples_txobject)))

    except Exception as e:
        logging.error(e)


    try:
        # ds_getransfer, ds_txobject = [], []
        # for x, y in zip( dur_gettransfers, samples_gettransfer):
        #     ds_getransfer.append({'x': x, 'y': y})
        # for x, y in zip(dur_txobject, samples_txobject):
        #     ds_txobject.append({'x': x, 'y': y})
        # ds_getransfer = str(ds_getransfer).replace('\'', '')
        # ds_txobject = str(ds_txobject).replace('\'', '')

        ds_getransfer, ds_txobject = readDbLog.preparedata_scatterplot()
        logging.info(ds_getransfer)
    except Exception as e:
        logging.error(e)


    return render_template('InsightsLog.html', dur_gettransfer=dur_gettransfers,samples_gettransfer=samples_gettransfer, dt_gettransfers=dt_gettransfers, dur_txobject=dur_txobject, samples_txobject=samples_txobject, ds_getransfer=ds_getransfer, ds_txobject=ds_txobject)


@app.route('/transactions')
def transactions():
    try:
        s = time()
        txs = dbManager.getTransactions()
        st = time()
        logging.info("fetching transactions from influxdb: {}".format(str(round(st - s, 3))))
    except Exception as e:
        logging.error(e)

    return render_template("Transactions.html", table_html=txs)


@app.route('/logs')
def logs():
    try:
        s = time()
        readDbLog, readSensorLog, readFlaskLog = LogReader("updatedatabase.log"), LogReader("sensor.log"), LogReader(
            "flask.log")
        dbLog, sensorLog, flaskLog = readDbLog.readlog(), readSensorLog.readlog(), readFlaskLog.readlog()
        st = time()
        logging.info("reading log files: {}".format(str(round(st - s, 3))))


    except Exception as e:
        logging.error(e)

    return render_template('Logs.html', databaselog=dbLog, sensorlog=sensorLog, flasklog=flaskLog)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
