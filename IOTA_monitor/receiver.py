from iota.crypto.types import Seed  #importing PyOTA library to interact with
from iota.crypto.addresses import AddressGenerator
import iota




devnet = "https://nodes.devnet.iota.org:443"

# # new seed
# newSeed = Seed.random()
# print(newSeed)

mySeed  = "EXSZTFGBBNOPETQGSZEOP9DUBQEFH9XKSB9RTRR9RFCCPLEQZAGEJ9LLYWSUAWWMLURNJBFWOPVWTLBWP"


api = iota.Iota(devnet,seed=mySeed )

addresses = api.get_new_addresses(index=0, count=3, security_level=2)

print(addresses)


