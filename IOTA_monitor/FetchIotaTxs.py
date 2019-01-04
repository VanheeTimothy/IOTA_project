from iota.commands.extended.utils import find_transaction_objects
import iota
from iota.adapter import BaseAdapter, HttpAdapter
import time



class FetchIotaTxs():
    def __init__(self, uriNet, mySeed, listTargetAdresses):
        self.api = iota.Iota(uriNet, seed=mySeed)
        self.uriNet = uriNet
        self.listAddr = listTargetAdresses


    def fetchTxs(self):
        return find_transaction_objects(adapter=HttpAdapter(self.uriNet), addresses=self.listAddr)

    def getSensorValue(self):
        values = []
        for Tx in self.fetchTxs():
            try:
                values.append(float(Tx.signature_message_fragment.decode()))
            except:
                pass

        return values







# api = iota.Iota(mainNet,seed=mySeed_mainNet)
#
#
# start = time.time()
# list_add = ["CPEIQD9UTUGPVBYRCUYYFISJARRBWNXBTANAINNYAVHJAOGTQWJGPORHXYXPVCJBH9XSVRCXVQHBFBNWD"]
# transactions = find_transaction_objects(adapter=aa,addresses=list_add)
# print("------------------------\n{}\n--------".format(transactions))
# i = 0
# for transaction in transactions:
#     print(transaction.signature_message_fragment.decode())
#     i+=1
# stop = time.time()
#
# print("duration: {}".format(stop-start))
# print("total tXs: {}".format(i))
# print("total txs in transactions {}".format(len(transactions)))