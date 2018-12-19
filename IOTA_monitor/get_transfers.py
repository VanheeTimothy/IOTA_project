# Gets all assosiated transactions from the saved addresses and saves the transaction data in the account file
from iota.commands.extended.utils import find_transaction_objects
import iota
from iota.adapter import BaseAdapter
from iota import Iota
import requests


iota_node = "https://nodes.devnet.iota.org:443"

def get_transfers(full_history, print_history=True):
    account_history_executing = True
    api = Iota(iota_node, seed)
    address_count = len(address_data)
    all_txn_hashes = []
    saved_txn_hashes = []
    new_txn_hashes = []
    i = 0

    while i < address_count:
        address = address_data[i]["address"]
        address_as_bytes = [bytes(address)]
        raw_transfers = api.find_transactions(addresses=address_as_bytes)
        transactions_to_check = raw_transfers["hashes"]

        for txn_hash in transactions_to_check:
            txn_hash = str(txn_hash)
            all_txn_hashes.append(txn_hash)
        i += 1

    for txn_hash in transfers_data:
        txn_hash = str(txn_hash['transaction_hash'])
        saved_txn_hashes.append(txn_hash)

    for txn_hash in all_txn_hashes:
        if txn_hash not in saved_txn_hashes:
            new_txn_hashes.append(txn_hash)

    if len(new_txn_hashes) > 0:
        print("Retreaving and saving transfer data from " + str(len(new_txn_hashes)) + " transaction(s)!\n"
                                                                                       "Please wait...\n")
        for txn_hash in new_txn_hashes:
            txn_hash_as_bytes = bytes(txn_hash)
            li_result = api.get_latest_inclusion(
                [txn_hash_as_bytes])  # Needs to be integrated into new transactions as well
            is_confirmed = li_result['states'][txn_hash]
            print(li_result)

            gt_result = api.get_trytes([txn_hash_as_bytes])
            trytes = str(gt_result['trytes'][0])
            txn = Transaction.from_tryte_string(trytes)
            timestamp = str(txn.timestamp)
            tag = str(txn.tag)
            address = str(txn.address)
            message = "some message"  # Placeholder untill message decoding is added
            value = str(txn.value)
            bundle = str(txn.bundle_hash)

            write_transfers_data(
                txn_hash,
                is_confirmed,
                timestamp,
                tag,
                address,
                message,
                value,
                bundle
            )

    if full_history:
        print_transaction_history(full_history, print_history)

    elif not full_history:
        print_transaction_history(full_history, print_history)


def call_history():
    if not account_history_executing:
        print("loop called for account history")
    get_transfers(full_history=False, print_history=False)