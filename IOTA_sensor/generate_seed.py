from iota.crypto.types import Seed  #importing PyOTA library to interact with
import iota

# new seed
newSeed = Seed.random()
print(newSeed)



mainNet = "https://nodes.thetangle.org:443"


# params devNet
devnet = "https://nodes.devnet.iota.org:443"

seed_main_sensor = "MNYQVXGXWEWPTUJRPJIFVZUXDKJVWPNFQSQSHESZUQLZICBUABBRFSC9JBCAUCGSRZHX99LTBVRYUBBCV"
seed_main_monitor = "CEKYETVXHVZOFEABGSTROBTGPGGGVSBMPYTDCTRCULBWRMDLFXQZ9CQBHUMWVKHOEYXQZG9DEWXJRMLCT"
target_addres = "OOJTC99SSUPQIQCPVDUBXR9HM9FBZ9PXPNJAWUVRWHEPJWIGUFERAJYWOZCDXRSICYLVRBBYNEXBTEEVD"


seed_DevNet = "FTQSBBKPGXFGBYOMWSAB9PIRSFWCJRAGHVVWGY9JJAOQQIMRVQCXWVWBGPYSRKWYBWUHMBEXRBSPHPCNN"
api = iota.Iota(mainNet,seed=seed_main_monitor )
addrs = api.get_new_addresses(index=1, count=1, security_level=2)
print(addrs)