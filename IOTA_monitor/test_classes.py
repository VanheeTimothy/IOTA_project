from FetchIotaTransfers import FetchIotaTranfers
from FetchIotaTxs import FetchIotaTxs
from time import time
import logging
logging.basicConfig(filename='testrun.log',level=logging.WARNING)

mainNet = "https://nodes.thetangle.org:443"
mySeed_mainNet = "9EJ9QUK9PJYJGNSOZPZLB99VMBQQPMYYFIMFPOFJHWIIPLFAELRYSVZCEXZRGLJHGUKLFZORQWZAZYPK9"
address_mainNet = "CPEIQD9UTUGPVBYRCUYYFISJARRBWNXBTANAINNYAVHJAOGTQWJGPORHXYXPVCJBH9XSVRCXVQHBFBNWD"

runs = 5

for i in range(1,runs+1):
    logging.warning("----------#RUN: "+str(i)+"----------")
    logging.warning("methode1: get_transfers")
    fetcher = FetchIotaTranfers(mainNet, mySeed_mainNet)
    start = time()
    data = fetcher.getValue()
    logging.warning(data)
    stop = time()
    logging.warning("duraction FetchIotaTransfers: " +str(stop-start))
    logging.warning("# datasamples: "+str(len(data)))
    logging.warning("methode2: find_transaction_objects")
    fetcher2 = FetchIotaTxs(mainNet, mySeed_mainNet, [address_mainNet])
    start = time()
    data2 = fetcher2.getSensorValue()
    logging.warning(data2)
    stop = time()
    logging.warning("duraction FetchIotaTxs: " +str(stop-start))
    logging.warning("# datasamples: "+str(len(data2)))

