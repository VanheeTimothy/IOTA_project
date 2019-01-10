from flask import Flask, render_template, request, session
import requests
from decimal import Decimal
import asyncio
from collections import defaultdict
from iota import Address, ProposedTransaction, Tag, Transaction
from time import time
import re
from iota.adapter import HttpAdapter
from FetchIotaTxs import FetchIotaTxs
from iota.crypto.types import Seed  #importing PyOTA library to interact with
from iota.crypto.addresses import AddressGenerator
import datetime
import pandas as pd
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_to_path = os.path.join(BASE_DIR, 'dummydata.txt')


def readDummyData(file_to_path):
    tempdata = []
    fo = open(file_to_path)
    c = 0
    for line in fo:
        line = line.rstrip("\n")
        if float(line) >25:
            c+=1
        tempdata.append(float(line))
    print(c)
    return tempdata



mainNet = "https://nodes.thetangle.org:443"
mySeed_mainNet = "9EJ9QUK9PJYJGNSOZPZLB99VMBQQPMYYFIMFPOFJHWIIPLFAELRYSVZCEXZRGLJHGUKLFZORQWZAZYPK9"
address_mainNet = "CPEIQD9UTUGPVBYRCUYYFISJARRBWNXBTANAINNYAVHJAOGTQWJGPORHXYXPVCJBH9XSVRCXVQHBFBNWD"

devnet = "https://nodes.devnet.iota.org:443"
address_devNet = b'TQJWJAD9MPSLOMUFZHMBKBYKPSSLLVILWAIEBKVIGOJDNE9DEFHB9KZROLRRQCOSEYVWEMO9TJURLZD9Y'
mySeed_devNet  = "EXSZTFGBBNOPETQGSZEOP9DUBQEFH9XKSB9RTRR9RFCCPLEQZAGEJ9LLYWSUAWWMLURNJBFWOPVWTLBWP"


test1 = FetchIotaTxs(devnet, mySeed_devNet, [address_devNet])

app = Flask(__name__)
@app.route('/')
def analytics():
    tempdata = test1.getSensorValue()
    # tempdata = readDummyData(file_to_path)   #dummy data

    print(len(tempdata))
    return render_template('Analytics.html', tempdata=tempdata)


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
    dd = test1.get_transactions_info()
    print(dd)
    Txs_len = len(dd["value"])
    print(Txs_len)
    # dd = {'value': [], 'tag': [], 'datetime': []}        # TODO delete dummy data
    df = pd.DataFrame.from_dict(dd)
    df_html = df.to_html( index=False).replace('border="1"','border="0"')
    return render_template("Transactions.html",table_html=df_html)



@app.route('/settings')
def settings():
    return render_template('Settings.html')




if __name__ == '__main__':
    app.run(debug=True)
