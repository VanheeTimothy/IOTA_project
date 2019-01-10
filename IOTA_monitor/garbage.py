from iota.crypto.types import Seed  #importing PyOTA library to interact with
from iota.crypto.addresses import AddressGenerator
import iota



# generate new seed
newSeed = Seed.random()
print(newSeed)

# seed devnet
devnet = "https://nodes.devnet.iota.org:443"
mySeed_devnet  = "EXSZTFGBBNOPETQGSZEOP9DUBQEFH9XKSB9RTRR9RFCCPLEQZAGEJ9LLYWSUAWWMLURNJBFWOPVWTLBWP"
mySeed_devnet_v2 = "FDRQXHXXCCJSTNRPRNOX9QXJFE9HR9JJQMCOUCBGR9DMTYUYFVPGXVCCUNMPHYKZ9ZKVICHNWTGQMUFIY"
# seed mainnet
mainNet = "https://nodes.thetangle.org:443"
mySeed_mainNet = "9EJ9QUK9PJYJGNSOZPZLB99VMBQQPMYYFIMFPOFJHWIIPLFAELRYSVZCEXZRGLJHGUKLFZORQWZAZYPK9"


api = iota.Iota(devnet,seed=mySeed_devnet )

addresses = api.get_new_addresses(index=0, count=3, security_level=2)

print(addresses["addresses"][0])



print("Checking for total balance. This may take some time...")

#
from time import time
# # now we can find out whether there are any tokens left
# start = time()
# SenderBalance = api.get_account_data(start=0,
#                                     stop=None)
# stop = time()
# duration = stop- start
# print("len="+str(duration))
s = time()
txs_of_addr = api.find_transactions(addresses=[addresses["addresses"][0]])
print(txs_of_addr)
TxsHashTail = txs_of_addr["hashes"][-1]
print(TxsHashTail)
# bundle = api.get_inputs(txs_of_addr["hashes"])
# print(bundle)
st = time()
print("duration" +str(st-s))
# print(SenderBalance)
#
# for dd in SenderBalance["bundles"]:
#     print(vars(dd))