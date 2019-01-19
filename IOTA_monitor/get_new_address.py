from iota.crypto.types import Seed  #importing PyOTA library to interact with
from iota.crypto.addresses import AddressGenerator
import iota



# generate new seed
newSeed = Seed.random()
print(newSeed)





# params devNet
devnet = "https://nodes.devnet.iota.org:443"
seed_DevNet = "FTQSBBKPGXFGBYOMWSAB9PIRSFWCJRAGHVVWGY9JJAOQQIMRVQCXWVWBGPYSRKWYBWUHMBEXRBSPHPCNN"
api = iota.Iota(devnet,seed=seed_DevNet )
addrs = api.get_new_addresses(index=1, count=1, security_level=2)
print(addrs)






# seed devnet
devnet = "https://nodes.devnet.iota.org:443"
mySeed_devnet  = "EXSZTFGBBNOPETQGSZEOP9DUBQEFH9XKSB9RTRR9RFCCPLEQZAGEJ9LLYWSUAWWMLURNJBFWOPVWTLBWP"
mySeed_devnet_v2 = "FDRQXHXXCCJSTNRPRNOX9QXJFE9HR9JJQMCOUCBGR9DMTYUYFVPGXVCCUNMPHYKZ9ZKVICHNWTGQMUFIY"
# seed mainnet
mainNet = "https://nodes.thetangle.org:443"
mySeed_mainNet = "9EJ9QUK9PJYJGNSOZPZLB99VMBQQPMYYFIMFPOFJHWIIPLFAELRYSVZCEXZRGLJHGUKLFZORQWZAZYPK9"


api = iota.Iota(devnet,seed=mySeed_devnet )

addresses = api.get_new_addresses(index=0, count=3, security_level=2)

print(addresses)
