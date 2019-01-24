import subprocess
from datetime import datetime
class LogReader():


    def __init__(self, filename):
        self.name = filename


    def readlog(self):
        with open('logs/'+str(self.name)) as f:
            logs = [x.rstrip() for x in f.readlines()]
        return logs


    def getDatapointsLog(self):
        dt_gettransfers, dur_gettransfers, samples_gettransfer, dt_txobject, dur_txobject, samples_txobject = [], [], [], [], [], []
        for line in self.readlog():
            try:
                from datetime import datetime

                levelname, u, m, s, method, value = line.split(":")
                date = str(u +":"+ m+":" + s)

                if method.strip() == "get_transfers duration":
                    dur_gettransfers.append(float(value.strip()))
                    dt_gettransfers.append(date)
                elif method.strip() == "get_transfers # samples":
                    samples_gettransfer.append(int(value.strip()))
                elif method.strip() == "find_transaction_objects duration":
                    dur_txobject.append(float(value.strip()))
                    dt_txobject.append(float(value.strip()))

                elif method.strip() == "find_transaction_objects # samples":
                    samples_txobject.append(int(value.strip()))
            except ValueError:
                pass

        return dt_gettransfers, dur_gettransfers, samples_gettransfer, dt_gettransfers, dur_txobject, samples_txobject


    def preparedata_scatterplot(self):
        gettransfer_data, txobject_data = [], []
        data_point = dict.fromkeys("x","y")
        for line in self.readlog():
            try:
                levelname, u, m, s, method, value = line.split(":")
                if method.strip() == "get_transfers duration":
                    data_point["y"] = float(value.strip())
                elif method.strip() == "get_transfers # samples":
                    data_point["x"] = int(value.strip())
                    gettransfer_data.append(data_point)
                    data_point = dict.fromkeys("x","y")
                elif method.strip() == "find_transaction_objects duration":
                    data_point["y"] = float(value.strip())
                elif method.strip() == "find_transaction_objects # samples":
                    data_point["x"] = int(value.strip())
                    txobject_data.append(data_point)
                    data_point = dict.fromkeys("x","y")
            except ValueError:
                pass

        gettransfer_data = str(gettransfer_data).replace('\'', '')
        txobject_data = str(txobject_data).replace('\'', '')

        return gettransfer_data, txobject_data

