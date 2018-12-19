from iota.commands.extended.utils import find_transaction_objects
import iota
from iota.adapter import BaseAdapter
from iota import Iota
import requests
devnet = "https://nodes.devnet.iota.org:443"

address = b'TQJWJAD9MPSLOMUFZHMBKBYKPSSLLVILWAIEBKVIGOJDNE9DEFHB9KZROLRRQCOSEYVWEMO9TJURLZD9Y'


mySeed  = "EXSZTFGBBNOPETQGSZEOP9DUBQEFH9XKSB9RTRR9RFCCPLEQZAGEJ9LLYWSUAWWMLURNJBFWOPVWTLBWP"
api = iota.Iota(devnet,seed=mySeed )
addresses = api.get_new_addresses(index=0, count=3, security_level=2)

tx = api.get_inputs()
print(addresses)
print(tx)
url = "https://devnet.thetangle.org/address/TQJWJAD9MPSLOMUFZHMBKBYKPSSLLVILWAIEBKVIGOJDNE9DEFHB9KZROLRRQCOSEYVWEMO9TJURLZD9Y"
response = requests.get(url)
adrfess_content  = response.json()
print(adrfess_content)
# transactions = find_transaction_objects(api,addresses=[iota.Address(address)])
#
# for transaction in transactions:
#   # Ignore input transactions; these have cryptographic signatures,
#   # not human-readable messages.
#   if transaction.value < 0:
#     continue
#
#   print(f'Message from {transaction.hash}:')
#
#   message = transaction.signature_message_fragment
#   if message is None:
#     print('(None)')
#   else:
#     print(message.decode())