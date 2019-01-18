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
            print(vars(Tx))
            try:
                values.append(float(Tx.signature_message_fragment.decode()))
            except:
                pass

        return values

    def getOneWireValue(self):
        values = []
        for Tx in self.fetchTxs():
            try:
                values.append(Tx.tag)
                print(str(Tx.tag).rstrip("9"))
            except Exception as e:
                print(e)
        return values

    def get_transactions_info(self):
        Txs = {"value": [], "tag": [], "datetime": []}
        try:
            for tx in self.fetchTxs():
                Txs["value"].append(float(tx.signature_message_fragment.decode()))
                Txs["tag"].append(str(tx.tag).strip("9"))
                Txs["datetime"].append(datetime.utcfromtimestamp(int(tx.timestamp)).strftime('%Y-%m-%d %H:%M:%S'))
                # Txs.append([float(tx.signature_message_fragment.decode()),
                #             str(tx.tag).strip("9"),
                #             datetime.utcfromtimestamp(int(tx.timestamp)).strftime('%Y-%m-%d %H:%M:%S')])
        except Exception as e:
            pass
        return Txs

    def get_querry_list(self):
        temp_data = []
        humm_data = []
        # Txs = {"value": [], "tag": [], "datetime": []}
        try:
            for tx in self.fetchTxs():
                if str(tx.tag).rstrip("9") == "DHTIOTA":
                    humm_data.append({"measurement":"hummidity",
                                      "tags":{
                                          "sensor":"DHT11"
                                      },
                                      "time":datetime.utcfromtimestamp(int(tx.timestamp)).strftime('%Y-%m-%d %H:%M:%S'),
                                      "fields":{
                                          "value": float(tx.signature_message_fragment.decode())
                                      }})
                    # temp_data.append('INSERT temperature, tag="onewire" value={} {}'.format(
                    #     float(tx.signature_message_fragment.decode()), tx.timestamp))
                else:
                    temp_data.append({"measurement":"temperature",
                                      "tags":{
                                          "sensor":"onewire"
                                      },
                                      "time":datetime.utcfromtimestamp(int(tx.timestamp)).strftime('%Y-%m-%d %H:%M:%S'),
                                      "fields":{
                                          "value": float(tx.signature_message_fragment.decode())
                                      }})
                    # humm_data.append('INSERT hummidity, tag="DHT11" value={} {}'.format(
                    #     float(tx.signature_message_fragment.decode()), tx.timestamp))

                    # humm_data.append({'measurement':"DHT11",
                    #                   'tag':str(tx.tag).strip("9"),
                    #                   'datetime':datetime.utcfromtimestamp(int(tx.timestamp)).strftime('%Y-%m-%d %H:%M:%S'),
                    #                   'fields':{
                    #                       'value': float(tx.signature_message_fragment.decode())
                    #                   }})
                    # humm_data.append({"value":float(tx.signature_message_fragment.decode()),
                    #                 "tag":str(tx.tag).strip("9"),
                    #                 "datetime":datetime.utcfromtimestamp(int(tx.timestamp)).strftime('%Y-%m-%d %H:%M:%S')})
                # else:
                    # temp_data.append({'measurement':"onewire",
                    #                   'tag':str(tx.tag).strip("9"),
                    #                   'datetime':datetime.utcfromtimestamp(int(tx.timestamp)).strftime('%Y-%m-%d %H:%M:%S'),
                    #                   'fields':{
                    #                       'value': float(tx.signature_message_fragment.decode())
                    #                   }})
                    # # temp_data.append({"value": float(tx.signature_message_fragment.decode()),
                    # #                   "tag": str(tx.tag).strip("9"),
                    # #                   "datetime": datetime.utcfromtimestamp(int(tx.timestamp)).strftime(
                    # #                       '%Y-%m-%d %H:%M:%S')})

        except Exception as e:
            pass
        return temp_data,humm_data










            # mainNet = "https://nodes.thetangle.org:443"
            # mySeed_mainNet = "9EJ9QUK9PJYJGNSOZPZLB99VMBQQPMYYFIMFPOFJHWIIPLFAELRYSVZCEXZRGLJHGUKLFZORQWZAZYPK9"
            # address_mainNet = "CPEIQD9UTUGPVBYRCUYYFISJARRBWNXBTANAINNYAVHJAOGTQWJGPORHXYXPVCJBH9XSVRCXVQHBFBNWD"
            # test1 = FetchIotaTxs(mainNet, mySeed_mainNet, [address_mainNet])
            # TxInfo = test1.get_transactions_info()
            # print(TxInfo)

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
