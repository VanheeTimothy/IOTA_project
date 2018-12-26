from flask import Flask, render_template, request
import requests
from decimal import Decimal
import asyncio
from collections import defaultdict
import iota
from iota import Address, ProposedTransaction, Tag, Transaction
from time import time
import re

from iota.crypto.types import Seed  #importing PyOTA library to interact with
from iota.crypto.addresses import AddressGenerator
import iota
import datetime

import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_to_path = os.path.join(BASE_DIR, 'dummydata.txt')

tempdata = []
def readDummyData(file_to_path):
    fo = open(file_to_path)
    c = 0
    for line in fo:
        line = line.rstrip("\n")
        if float(line) >25:
            c+=1
        tempdata.append(float(line))
    print(c)
readDummyData(file_to_path)

app = Flask(__name__)
@app.route('/')
def analytics():
    return render_template('Analytics.html', tempdata=tempdata)

@app.route('/transactions')
def transactions():
    return render_template('Transactions.html')

@app.route('/settings')
def settings():
    return render_template('Settings.html')




if __name__ == '__main__':
    app.run(debug=True)
