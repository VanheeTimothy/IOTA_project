import requests
from decimal import Decimal

from collections import defaultdict
import iota
from iota import Address, ProposedTransaction, Tag, Transaction
from time import time
from iota.adapter import HttpAdapter
from iota.crypto.types import Seed  #importing PyOTA library to interact with
from iota.crypto.addresses import AddressGenerator
import iota
import datetime
from iota.commands.extended.utils import iter_used_addresses


devnet = "https://nodes.devnet.iota.org:443"
mainNet = "https://nodes.thetangle.org:443"
# # new seed
# newSeed = Seed.random()
# print(newSeed)

address_devNet = b'TQJWJAD9MPSLOMUFZHMBKBYKPSSLLVILWAIEBKVIGOJDNE9DEFHB9KZROLRRQCOSEYVWEMO9TJURLZD9Y'
mySeed_devNet  = "EXSZTFGBBNOPETQGSZEOP9DUBQEFH9XKSB9RTRR9RFCCPLEQZAGEJ9LLYWSUAWWMLURNJBFWOPVWTLBWP"
mySeed_mainNet = "9EJ9QUK9PJYJGNSOZPZLB99VMBQQPMYYFIMFPOFJHWIIPLFAELRYSVZCEXZRGLJHGUKLFZORQWZAZYPK9"
address_mainNet = "CPEIQD9UTUGPVBYRCUYYFISJARRBWNXBTANAINNYAVHJAOGTQWJGPORHXYXPVCJBH9XSVRCXVQHBFBNWD"



api = iota.Iota(mainNet,seed=mySeed_mainNet)

# addresses = api.get_new_addresses(index=0, count=3, security_level=2)
# print(addresses)



start =  time()
print(start)
transactions = api.find_transactions(addresses=[address_mainNet])# use index otherwise loadtime = very slow
stop = time()
print(stop)
print(transactions)

transaction_list  = []
for tx in transactions["hashes"]:
    # print(tx)
    # print(type(tx))
    transaction_list.append(tx)
    # for tx in bundle:
    #     print(vars(tx))
    #     print(tx.signature_message_fragment.decode())


# print(transaction_objects)
# print(vars(transaction_objects))
# print("duration :" +str(stop-start))
# print(len(transactions["hashes"]))

# test =iter_used_addresses(mainNet,seed="QG9PRLCNUGJRE9XLJUXJLP9ZQKBSCQXCDMWHWZWYSVMYFXYWDSJFTTUMVMFHKUSJNJATWUFVIKUPVPVIN",start=0)
print(transaction_list)
