from flask import Flask, render_template, request
import requests
from decimal import Decimal
import asyncio
from collections import defaultdict
import iota
from iota import Address, ProposedTransaction, Tag, Transaction
from time import time


from iota.crypto.types import Seed  #importing PyOTA library to interact with
from iota.crypto.addresses import AddressGenerator
import iota
import datetime



devnet = "https://nodes.devnet.iota.org:443"
mainNet = "https://nodes.thetangle.org:443"
# # new seed
# newSeed = Seed.random()
# print(newSeed)

address_devNet = b'TQJWJAD9MPSLOMUFZHMBKBYKPSSLLVILWAIEBKVIGOJDNE9DEFHB9KZROLRRQCOSEYVWEMO9TJURLZD9Y'
mySeed_devNet  = "EXSZTFGBBNOPETQGSZEOP9DUBQEFH9XKSB9RTRR9RFCCPLEQZAGEJ9LLYWSUAWWMLURNJBFWOPVWTLBWP"
mySeed_mainNet = "9EJ9QUK9PJYJGNSOZPZLB99VMBQQPMYYFIMFPOFJHWIIPLFAELRYSVZCEXZRGLJHGUKLFZORQWZAZYPK9"
address_mainNet = "CPEIQD9UTUGPVBYRCUYYFISJARRBWNXBTANAINNYAVHJAOGTQWJGPORHXYXPVCJBH9XSVRCXVQHBFBNWD"



api = iota.Iota(mainNet,seed=mySeed_mainNet )

addresses = api.get_new_addresses(index=0, count=3, security_level=2)
data = []
async  def getTempData():
    accountData = api.get_transfers(start=1, stop=2)  # use index otherwise loadtime = very slow
    for bundle in accountData["bundles"]:
        for tx in bundle:
            print(vars(tx))
            print(tx.signature_message_fragment.decode())
            data.append(tx.signature_message_fragment.decode())
async def getdata():
    return await getTempData()




app = Flask(__name__)
tempData = getTempData()
@app.route('/')
def analytics():
    getdata()

    return render_template('Analytics.html',tempvalue=data)

@app.route('/transactions')
def transactions():
    return render_template('Transactions.html')

@app.route('/settings')
def settings():
    return render_template('Settings.html')




if __name__ == '__main__':
    app.run(debug=True)
