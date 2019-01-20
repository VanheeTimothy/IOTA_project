from iota.commands.extended.utils import find_transaction_objects
import iota
from iota.adapter import BaseAdapter, HttpAdapter
import time
from datetime import datetime
import credentials

class FetchIotaTxs():
    def __init__(self, uriNet, mySeed, listTargetAdresses):
        self.api = iota.Iota(uriNet, seed=mySeed)
        self.uriNet = uriNet
        self.listAddr = listTargetAdresses

    def fetchTxs(self):
        return find_transaction_objects(adapter=HttpAdapter(self.uriNet), addresses=self.listAddr)


    def get_querry_list(self):
        temp_data = []
        humm_data = []
        try:
            for tx in self.fetchTxs():
                print(vars(tx))
                if str(tx.tag).rstrip("9") == "DHTIOTA":
                    humm_data.append({"measurement":"hummidity",
                                      "tags":{
                                          "sensor":"DHT11",
                                          "hash": tx.hash
                                      },
                                      "time":datetime.utcfromtimestamp(int(tx.timestamp)).strftime('%Y-%m-%d %H:%M:%S'),
                                      "fields":{
                                          "value": float(tx.signature_message_fragment.decode())
                                      }})

                else:
                    temp_data.append({"measurement":"temperature",
                                      "tags":{
                                          "sensor":"DS18B20",
                                          "hash":tx.hash
                                      },
                                      "time":datetime.utcfromtimestamp(int(tx.timestamp)).strftime('%Y-%m-%d %H:%M:%S'),
                                      "fields":{
                                          "value": float(tx.signature_message_fragment.decode())
                                      }})

        except Exception as e:
            pass
        return temp_data,humm_data


if __name__ == '__main__':
    mainNet = "https://nodes.thetangle.org:443"
    seed_main_monitor = credentials.login["seed_main_monitor"]
    target_address = credentials.login["target_address"]
    test1 = FetchIotaTxs(mainNet, seed_main_monitor, [target_address])
    temp_data, humm_data = test1.get_querry_list()