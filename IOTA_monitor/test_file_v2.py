from iota.commands.extended.utils import find_transaction_objects
import iota
from iota.adapter import BaseAdapter, HttpAdapter
import time

aa = HttpAdapter("https://nodes.thetangle.org:443")
mainNet = "https://nodes.thetangle.org:443"
mySeed_mainNet = "9EJ9QUK9PJYJGNSOZPZLB99VMBQQPMYYFIMFPOFJHWIIPLFAELRYSVZCEXZRGLJHGUKLFZORQWZAZYPK9"
address_mainNet = "CPEIQD9UTUGPVBYRCUYYFISJARRBWNXBTANAINNYAVHJAOGTQWJGPORHXYXPVCJBH9XSVRCXVQHBFBNWD"

api = iota.Iota(mainNet,seed=mySeed_mainNet)


start = time.time()
list_add = ["CPEIQD9UTUGPVBYRCUYYFISJARRBWNXBTANAINNYAVHJAOGTQWJGPORHXYXPVCJBH9XSVRCXVQHBFBNWD"]
transactions = find_transaction_objects(adapter=aa,addresses=list_add)
print("------------------------\n{}\n--------".format(transactions))
i = 0
for transaction in transactions:
    print(transaction.signature_message_fragment.decode())
    i+=1
stop = time.time()

print("duration: {}".format(stop-start))
print("total tXs: {}".format(i))
print("total txs in transactions {}".format(len(transactions)))