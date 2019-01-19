from time import time
from flask import Flask, render_template
from influxdb import InfluxDBClient
from model.Logreader import LogReader
import logging

logging.basicConfig(filename='logs/flask.log', level=logging.INFO, format='%(levelname)s %(asctime)s %(message)s')



try:

    start = time()
    port = 8086
    host = 'localhost'
    dbname ="sensorvaluesiota"
    client = InfluxDBClient(host=host, port=port)
    client.switch_database(dbname)
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
        temp = client.query('SELECT "value" FROM temperature')
        humm = client.query('SELECT "value" FROM hummidity ')
        st = time()
        print("duration: " + str(st-s))
        logging.info("fetching temp and humm values from influxdb: {}s".format(round(st-s,3)))
        temp_raw, humm_raw = temp.raw["series"][0]["values"], humm.raw["series"][0]["values"]
        temp_points, humm_points = [l[1] for l in temp_raw], [l[1] for l in humm_raw]

    except Exception as e:
        logging.error(e)

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
    try:
        s = time()
        temp, humm = client.query('SELECT * FROM temperature'), client.query('SELECT * FROM hummidity ')
        humm_raw, temp_raw = humm.raw["series"][0]["values"], temp.raw["series"][0]["values"]
        print(humm_raw)
        table_data = sorted(humm_raw + temp_raw)  # TODO sort values when None is
        st = time()
        logging.info("fetching transactions from influxdb: {}".format(str(round(st - s, 3))))
    except Exception as e:
        logging.error(e)

    return render_template("Transactions.html",table_html=table_data)



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
