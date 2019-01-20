from iota.crypto.types import Seed
import logging
import iota


logging.basicConfig(filename='logs/generateseed.log', level=logging.INFO, format='%(levelname)s %(asctime)s %(message)s')

# generate new seed
newSeed = Seed.random()

logging.info("generate seed: {}".format(newSeed))
devnet = "https://nodes.devnet.iota.org:443"
mainNet = "https://nodes.thetangle.org:443"


api = iota.Iota(devnet,seed=newSeed )
addresses = api.get_new_addresses(index=0, count=1, security_level=2)
logging.info(addresses["addresses"])
