from iota.crypto.types import Seed  #importing PyOTA library to interact with
from iota.crypto.addresses import AddressGenerator
import iota
import datetime
from pprint import pprint
from time import time

devnet = "https://nodes.devnet.iota.org:443"
mainNet = "https://nodes.thetangle.org:443"
# new seed
newSeed = Seed.random()
print(newSeed)

mySeed_devnet = "SAEWHQJPUIGDKLB9FQ9XTNYZTWRRYVLZAFMGRYYNAFIEMUWNUADVTZTMLYQCLPSJVKJHZTSMYZWWIFXSW"
targetAddress_devnet = b'TQJWJAD9MPSLOMUFZHMBKBYKPSSLLVILWAIEBKVIGOJDNE9DEFHB9KZROLRRQCOSEYVWEMO9TJURLZD9Y'

mySeed_mainNet = "QG9PRLCNUGJRE9XLJUXJLP9ZQKBSCQXCDMWHWZWYSVMYFXYWDSJFTTUMVMFHKUSJNJATWUFVIKUPVPVIN"
targetAddress_mainNet = "JMZQEQFYKVLZXHXUQLOYQZWHWI9VGTLR9LJVYCONEDLZHBBUVFZHDKR9WHN9LNDGZMXYKQFNJGHKROLLA"

api = iota.Iota(mainNet,seed=mySeed_mainNet )

addresses = api.get_new_addresses(index=0, count=3, security_level=2)

print(addresses)

nowIs = datetime.datetime.now()

def prepare_transaction(targetAddress, msg,tag, value):
    # preparing a transaction
    pt = iota.ProposedTransaction(address=iota.Address(targetAddress),
                                  message=iota.TryteString.from_unicode(str(msg+' %s') % (nowIs)),
                                  tag=iota.Tag(bytes(tag, 'utf8')),
                                  value=value)
    return pt

def prepare_bundle(Tx_list):
    # preparing bundle
    pb = iota.ProposedBundle(transactions=Tx_list)
    pb.finalize()
    return pb

def get_tips_to_approve():
    return api.get_transactions_to_approve(depth=3)

def do_POW(bundleAsTrytes, getApprovedTips):
    return api.attach_to_tangle(trunk_transaction=getApprovedTips["trunkTransaction"],
                                          branch_transaction=getApprovedTips["branchTransaction"],
                                          trytes=bundleAsTrytes,
                                          min_weight_magnitude=14)  # MWMW for devNet = 9
                                                                    # MWMW for mainNet = 14


start = time()
# STEP1: prepare transaction(s)
pt = prepare_transaction(targetAddress_mainNet, '18.06','RASPBERRYHOWESTIOTA',0)
pt1 = prepare_transaction(targetAddress_mainNet, "18.09", "RASPBERRYHOWESTIOTA",0)
print("Creating transaction objects :")
print(vars(pt))


# # STEP2: all Txs needs to get in a bundle (even if it's a single Tx)
# pb = prepare_bundle([pt, pt1])
# print("generated bundle hash: %s"%(pb.hash))
# print("tail transaction in the bundle is a transaction #%s"%(pb.tail_transaction.current_index))
# # convert bundle as Trytes
# bundleAsTrytes = pb.as_tryte_strings()
#
#
# # STEP3: get tips to approve on the Tangle
# getApprovedTips = get_tips_to_approve()
# print(getApprovedTips)
#
#
# # STEP4: do proof of work
# print("Performing POW... please wait..\n")
# attachToTangle = do_POW(bundleAsTrytes, getApprovedTips)
# print(attachToTangle)
#
# # show what has been broadcasted - hash transaction + nonce (POW)
# for t in attachToTangle["trytes"]:
#     print(vars(iota.Transaction.from_tryte_string(t)))
#     print("---")
#
#
# # STEP5: broadcast Txs and store
# print("broadcasting transaction...")
# res = api.broadcast_and_store(attachToTangle["trytes"])
# print(res)
# stop = time()
#
# print(stop-start)
# the whole process initiated in a single call
start = time()
FinalBundle = api.send_transfer(depth=3,
                                transfers=[pt, pt1],
                                min_weight_magnitude=14)['bundle']  # it returns a dictionary with a bundle object
stop = time()
for txn in FinalBundle:
    pprint(vars(txn))
    print("")


print("duration: "+str(stop-start))