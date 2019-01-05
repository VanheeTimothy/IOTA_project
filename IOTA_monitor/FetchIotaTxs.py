from iota.commands.extended.utils import find_transaction_objects
import iota
from iota.adapter import BaseAdapter, HttpAdapter
import time
from datetime import datetime


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


    def get_transactions_info(self):
        Txs= []
        try:
            for tx in self.fetchTxs():
                Txs.append((float(tx.signature_message_fragment.decode()),
                            str(tx.tag).strip("9"),
                            datetime.utcfromtimestamp(int(tx.timestamp)).strftime('%Y-%m-%d %H:%M:%S')))
        except Exception as e:
            print(e)
        return sorted(Txs, key=lambda tup: tup[2])






mainNet = "https://nodes.thetangle.org:443"
mySeed_mainNet = "9EJ9QUK9PJYJGNSOZPZLB99VMBQQPMYYFIMFPOFJHWIIPLFAELRYSVZCEXZRGLJHGUKLFZORQWZAZYPK9"
address_mainNet = "CPEIQD9UTUGPVBYRCUYYFISJARRBWNXBTANAINNYAVHJAOGTQWJGPORHXYXPVCJBH9XSVRCXVQHBFBNWD"
test1 = FetchIotaTxs(mainNet, mySeed_mainNet, [address_mainNet])
TxInfo = test1.get_transactions_info()
print(vars(TxInfo))

# print(TxInfo[0])
#
# for tx in TxInfo:
#     print(str(tx["tag"]).strip("9"))
#     print(datetime.utcfromtimestamp(int(tx["timestamp"])).strftime('%Y-%m-%d %H:%M:%S'))
#     print(str(tx["signature_message_fragment"].decode()))


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