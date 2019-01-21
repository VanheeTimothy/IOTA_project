from influxdb import InfluxDBClient
from datetime import datetime, timedelta




class DatabaseManager():



    def __init__(self, host, port, dbname):
        self.client = client = InfluxDBClient(host=host, port=port)
        client.switch_database(dbname)





    def getSensorData(self,timeSpan=None):
        # if timeSpan=="today":
        temp = self.client.query('SELECT "time", "value" FROM temperature')
        humm = self.client.query('SELECT "time", "value" FROM hummidity ')
        temp_raw, humm_raw = temp.raw["series"][0]["values"], humm.raw["series"][0]["values"]
        temp_points, humm_points = [l[1] for l in temp_raw], [l[1] for l in humm_raw]
        labels = [l[0] for l in humm_raw]
        return temp_points, humm_points, labels


    def getTransactions(self):
        temp, humm = self.client.query('SELECT * FROM temperature'), self.client.query('SELECT * FROM hummidity ')
        humm_raw, temp_raw = humm.raw["series"][0]["values"], temp.raw["series"][0]["values"]
        return sorted(humm_raw + temp_raw)

    # def
    def getSensorDatatest(self, timeSpan=None):
        startTime = datetime.now() - timedelta(days=1)
        endTime = datetime.now()
        str_st = str(startTime)
        str_end = str(endTime)
        print(startTime)
        data = self.client.query('select * from temperature where time >= {} and time <= {} '%(str_st,str_end))
        d = data.raw["series"][0]["values"]
        return d