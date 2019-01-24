from influxdb import InfluxDBClient
from datetime import datetime, timedelta




class DatabaseManager():



    def __init__(self, host, port, dbname):
        self.client = InfluxDBClient(host=host, port=port)
        self.client.switch_database(dbname)





    def getAllSensorData(self):
        temp = self.client.query('SELECT "time", "value" FROM temperature')
        hum = self.client.query('SELECT "time", "value" FROM humidity')
        temp_raw, hum_raw = temp.raw["series"][0]["values"], hum.raw["series"][0]["values"]
        temp_points, hum_points = [l[1] for l in temp_raw], [l[1] for l in hum_raw]
        labels = [l[0] for l in hum_raw]
        return temp_points, hum_points, labels



    def getSensorDataTimespan(self, timeSpan=1):
        endTime = datetime.now()
        startTime = endTime - timedelta(days=timeSpan)
        str_st, str_end = "'" + str(startTime) + "'", "'" + str(
            endTime) + "'"
        temp = self.client.query(('select "time", "value" from temperature where time >= {} and time <= {} ').format(str_st, str_end))
        hum = self.client.query(('select "time", "value" from humidity where time >= {} and time <= {} ').format(str_st, str_end))
        temp_raw, hum_raw = temp.raw["series"][0]["values"], hum.raw["series"][0]["values"]
        temp_points, hum_points = [l[1] for l in temp_raw], [l[1] for l in hum_raw]
        labels = [l[0] for l in hum_raw]
        return  temp_points, hum_points, labels


    def getTransactions(self):
        temp, hum = self.client.query('SELECT * FROM temperature'), self.client.query('SELECT * FROM humidity')
        hum_raw, temp_raw = hum.raw["series"][0]["values"], temp.raw["series"][0]["values"]
        return sorted(hum_raw + temp_raw)








