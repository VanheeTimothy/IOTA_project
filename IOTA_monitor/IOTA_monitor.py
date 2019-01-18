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

port = 8086
host = 'localhost'
client = InfluxDBClient(host=host,port=port)
client.switch_database("sensorvaluesiota")





app = Flask(__name__)
@app.route('/')
def analytics():
    s = time()
    data = client.query('SELECT "value" FROM temperature')
    st = time()
    print(data)
    print("duration: " + str(st-s))


    return render_template('Analytics.html', tempdata=data.raw["series"][0]["values"])


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
    # dd = test1.get_transactions_info()
    # print(dd)
    # Txs_len = len(dd["value"])
    # print(Txs_len)
    # # dd = {'value': [], 'tag': [], 'datetime': []}        # TODO delete dummy data
    # df = pd.DataFrame.from_dict(dd)
    # df_html = df.to_html( index=False).replace('border="1"','border="0"')
    return render_template("Transactions.html",table_html=df_html)



@app.route('/settings')
def settings():
    return render_template('Settings.html')




if __name__ == '__main__':
    app.run(debug=True)
