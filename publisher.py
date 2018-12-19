from iota.crypto.types import Seed  #importing PyOTA library to interact with
from iota.crypto.addresses import AddressGenerator
import iota
NewSeed = Seed.random()

my_seed = b'ZNYAVKBBBNCQUQ9DUSDDGSRITTNGINCHSYCN9IMLZCNE9DZA9UCS9YZDDDWEQQYSALMPPSJVLERICVPWL'



print("Length: %s" % len(NewSeed))

generator = AddressGenerator(seed=my_seed,
                             security_level=2)

result = generator.get_addresses(0, 3)
print(result[0])

def validateAddress(addressIncChecksum):
    address = iota.Address(addressIncChecksum)
    isValid = address.is_checksum_valid() # it is a good practise to encourage user of your app using IOTA addresses including checksums = 90 trytes
    return isValid


result[0] = result[0].with_valid_checksum()
print(validateAddress(result[0]))
print(validateAddress("CVNRSOAXYHASNPQNVWLPUDZGAFFTEGP9BVRVTEROEG9HKXUDZGDYXCGWYIPEFNJJDNNIQTZQZODRMMTC9"))
print(validateAddress(b"XYJV9DRIE9NCQJYLOYOJOGKQGOOELTWXVWUYGQSWCNODHJAHACADUAAHQ9ODUICCESOIVZABA9LTMM9RW"))
