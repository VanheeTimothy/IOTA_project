import iota

class TransferIotaTxs():

    def __init__(self, endpoint, seed):
        self.api = iota.Iota(endpoint, seed=seed)

    def prepare_transaction(self, targetAddress, msg, tag, value):
        # preparing a transaction
        pt = iota.ProposedTransaction(address=iota.Address(targetAddress),
                                      message=iota.TryteString.from_unicode(str(msg)),
                                      tag=iota.Tag(bytes(tag, 'utf8')),
                                      value=value)
        return pt

    def send_transfers(self, depth, transfers, weight):
        FinalBundle = self.api.send_transfer(depth=depth,
                                    transfers=transfers,
                                    min_weight_magnitude=weight)[
        'bundle']  # it returns a dictionary with a bundle object
        return FinalBundle

