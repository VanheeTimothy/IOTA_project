from iota.crypto.types import Seed  #importing PyOTA library to interact with
import iota

# new seed
newSeed = Seed.random()
print(newSeed)



mainNet = "https://nodes.thetangle.org:443"


# params devNet
devnet = "https://nodes.devnet.iota.org:443"

seed_main_sensor = "IDUDSATZD9WETVXYWZDS9MEENDOLLIRBQMXOVZCZLILFCTJN9VXAQXVZEATMG9PBOTUNULNDVMWBHJJEE"
seed_main_monitor = "VUACIICSQQSDYDTH9FBSPKULYZGQWAMFSZAOTOTE9IIYDJUFZHZR9EHYMRWCEUTOKPWXVTSDKN9F999JA"
target_addres = "9PGAPJOUSVS9TVTLVYNMWEJIMBQVKAYKF9CMGVN9SINNLUDJFVDJCGN9JTJ9SCW9HWMCRCKHCSJPSPDZD"


seed_DevNet = "FTQSBBKPGXFGBYOMWSAB9PIRSFWCJRAGHVVWGY9JJAOQQIMRVQCXWVWBGPYSRKWYBWUHMBEXRBSPHPCNN"
api = iota.Iota(mainNet,seed=seed_main_monitor )
addrs = api.get_new_addresses(index=1, count=1, security_level=2)
print(addrs)