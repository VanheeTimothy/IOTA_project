from iota.commands.extended.utils import find_transaction_objects
import iota
from iota.adapter import BaseAdapter, HttpAdapter
import time
from datetime import datetime
import sys

sys.path.append("..")


class FetchIotaTxs():
    def __init__(self, uriNet, mySeed, listTargetAdresses):
        self.api = iota.Iota(uriNet, seed=mySeed)
        self.uriNet = uriNet
        self.listAddr = listTargetAdresses

    def fetchTxs_fto(self):
        return find_transaction_objects(adapter=HttpAdapter(self.uriNet), addresses=self.listAddr)

    def fetchTxs_get_transfer(self):
        return self.api.get_transfers(start=0, stop=3)

    def get_querry_list(self, methode=0):
        methode = self.fetchTxs_get_transfer()["bundles"]
        if methode == 0:
            methode = self.fetchTxs_fto()
        temp_data, humm_data = [], []

        for bundle in methode:
            for tx in bundle:
                if str(tx.tag).rstrip("9") == "DHTIOTA":
                    humm_data.append({"measurement": "humidity",
                                      "tags": {
                                          "sensor": "DHT11",
                                          "hash": tx.hash
                                      },
                                      "time": datetime.utcfromtimestamp(int(tx.timestamp)).strftime(
                                          '%Y-%m-%d %H:%M:%S'),
                                      "fields": {
                                          "value": float(tx.signature_message_fragment.decode())
                                      }})
                else:
                    temp_data.append({"measurement": "temperature",
                                      "tags": {
                                          "sensor": "DS18B20",
                                          "hash": tx.hash
                                      },
                                      "time": datetime.utcfromtimestamp(int(tx.timestamp)).strftime(
                                          '%Y-%m-%d %H:%M:%S'),
                                      "fields": {
                                          "value": float(tx.signature_message_fragment.decode())
                                      }})

        return temp_data, humm_data




