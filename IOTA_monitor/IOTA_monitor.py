from time import time

# import pandas as pd
from flask import Flask, render_template
from influxdb import InfluxDBClient

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
    temp = client.query('SELECT * FROM temperature')
    humm = client.query('SELECT "value" FROM hummidity ')
    humm_raw = humm.raw["series"][0]["values"]

    temp_raw = temp.raw["series"][0]["values"]
    table_data = humm_raw + temp_raw
    # formatted_temp = simpletable.fit_data_to_columns(temp_raw, 3)
    # temp_table = simpletable.SimpleTable(formatted_temp)
    # temp_html = simpletable.HTMLPage(temp_table)


    # dd = test1.get_transactions_info()
    # print(dd)
    # Txs_len = len(dd["value"])
    # print(Txs_len)
    # # dd = {'value': [], 'tag': [], 'datetime': []}        # TODO delete dummy data
    # df = pd.DataFrame.from_dict(dd)
    # df_html = df.to_html( index=False).replace('border="1"','border="0"')
    return render_template("Transactions.html",table_html=table_data)



@app.route('/logs')
def logs():
    return render_template('Logs.html')




if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
