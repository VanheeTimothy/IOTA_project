import requests
from decimal import Decimal

from collections import defaultdict
import iota
from iota import Address, ProposedTransaction, Tag, Transaction
from time import time

devnet = "https://nodes.devnet.iota.org:443"
address1 = b'TQJWJAD9MPSLOMUFZHMBKBYKPSSLLVILWAIEBKVIGOJDNE9DEFHB9KZROLRRQCOSEYVWEMO9TJURLZD9Y'
mySeed  = "EXSZTFGBBNOPETQGSZEOP9DUBQEFH9XKSB9RTRR9RFCCPLEQZAGEJ9LLYWSUAWWMLURNJBFWOPVWTLBWP"
api = iota.Iota(devnet,seed=mySeed )


start =  time()
print(start)
accountData = api.get_account_data()
print(accountData)
stop = time()
print(stop)



for bundle in accountData["bundles"]:
    for tx in bundle:
        print(tx.signature_message_fragment.decode())


print("duration :" +str(stop-start))



