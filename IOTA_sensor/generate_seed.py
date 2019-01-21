from iota.crypto.types import Seed  #importing PyOTA library to interact with
import iota

# new seed
newSeed = Seed.random()


mainNet = "https://nodes.thetangle.org:443"
devnet = "https://nodes.devnet.iota.org:443"

api = iota.Iota(mainNet,seed=newSeed )
addrs = api.get_new_addresses(index=1, count=1, security_level=2)


print(newSeed)
print(addrs)