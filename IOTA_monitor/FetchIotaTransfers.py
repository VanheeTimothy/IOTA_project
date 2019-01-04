from time import time
from iota.commands.extended.utils import find_transaction_objects
import iota
from iota.adapter import BaseAdapter, HttpAdapter




class FetchIotaTranfers():
    def __init__(self, uriNet, mySeed):
        self.api = iota.Iota(uriNet, seed=mySeed)

    def transferData(self, start,stop):
        return self.api.get_transfers(start=start,stop=stop)

    def getValue(self):
        values = []
        # start = time()
        for bundle in self.transferData(0,3)["bundles"]:
            for tx in bundle:
                # print(vars(tx))
                values.append(tx.signature_message_fragment.decode())
        # stop = time()
        # print("duration: "+str(stop-start))
        return values







# # api = iota.Iota(mainNet,seed=mySeed_mainNet)
# # start = time()
# # accountData = api.get_transfers(start=0,stop=3)
# # stop = time()
# #
# # print(accountData)
# # c = 0
# # for bundle in accountData["bundles"]:
# #     for tx in bundle:
# #         print(tx.signature_message_fragment.decode())
# #         c+=1
# # print("duration :"+str(stop-start))
# # print(len(accountData["bundles"]))
# print("count: "+str(c))
