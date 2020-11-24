import argparse

import base58

import utils
from wallet import Wallet
from wallets import Wallets
from pow import Pow
from blockchain import Blockchain
from transaction import UTXOTx, CoinbaseTx
from utxo_set import UTXOSet


def new_parser():
    parser = argparse.ArgumentParser()
    sub_parser = parser.add_subparsers(help='commands')
    # A print command
    printchain_parser = sub_parser.add_parser(
        'printchain', help='Print all the blocks of the blockchain')
    printchain_parser.add_argument('--print', dest='printchain', action='store_true')
    # A print comman
    printblock_parser = sub_parser.add_parser(
        'printblock', help='Print a block with the HEIGHT in the blockchain')
    printblock_parser.add_argument('--height', type=int, dest='block_height', help='HEIGHT of the block')

    # A getbalance command
    balance_parser = sub_parser.add_parser(
        'getbalance', help='Get balance of ADDRESS')
    balance_parser.add_argument(
        '--address', type=str, dest='balance_address', help='ADDRESS of balance')
    # A createblockchain command
    bc_parser = sub_parser.add_parser(
        'createblockchain', help='Create a blockchain and send genesis block reward to ADDRESS')
    bc_parser.add_argument(
        '--address', type=str, dest='blockchain_address', help='ADDRESS')
    # A send command
    send_parser = sub_parser.add_parser(
        'send', help='Send AMOUNT of coins from FROM address to TO')
    send_parser.add_argument(
        '--from', type=str, dest='send_from', help='FROM')
    send_parser.add_argument(
        '--to', type=str, dest='send_to', help='TO')
    send_parser.add_argument(
        '--amount', type=int, dest='send_amount', help='AMOUNT')

    # A createwallet command
    bc_parser = sub_parser.add_parser(
        'createwallet', help='Create a wallet')
    bc_parser.add_argument(
        '--wallet', type=str, dest='wallet', help='WALLET')

    return parser


def get_balance(address):
    bc = Blockchain()
    utxo_set = UTXOSet(bc)

    utxo_set.print_utxo()

    pubkey_hash = utils.address_to_pubkey_hash(address)
    utxos = utxo_set.find_utxo(pubkey_hash)
    balance = 0

    for out in utxos:
        balance += out.value

    print('Balance of {0}: {1}'.format(address, balance))


def create_blockchain(address):
    bc = Blockchain(address)
    utxo_set = UTXOSet(bc)
    utxo_set.reindex()

    print('Done!')


def create_wallet():
    wallets = Wallets()
    wallet = Wallet()
    address = wallet.address
    wallets.add_wallet(address, wallet)
    wallets.save_to_file()

    print("Your new address: {}".format(address))


def print_chain():
    bc = Blockchain()

    for block in bc.blocks:
        print("Prev. hash: {0}".format(block.prev_block_hash))
        print("Hash: {0}".format(block.hash))
        print("Height: {0}".format(block.height))
        pow = Pow(block)
        print("PoW: {0}".format(pow.validate()))

def print_block(height):
    bc = Blockchain()

    for block in bc.blocks:
        if(block.height == height):
            print("Prev. hash: {0}".format(block.prev_block_hash))
            print("Hash: {0}".format(block.hash))
            print("Height: {0}".format(block.height))
            pow = Pow(block)
            print("PoW: {0}".format(pow.validate()))
            break


def send(from_addr, to_addr, amount):
    bc = Blockchain()
    utxo_set = UTXOSet(bc)

    tx = UTXOTx(from_addr, to_addr, amount, utxo_set)
    cb_tx = CoinbaseTx(from_addr)
    new_block = bc.MineBlock([cb_tx, tx])
    utxo_set.update(new_block)
    print('Success!')


if __name__ == '__main__':
    parser = new_parser()
    args = parser.parse_args()

    if hasattr(args, 'wallet'):
        create_wallet()

    if hasattr(args, 'printchain'):
        print_chain()
    
    if hasattr(args, 'block_height'):
        print_block(args.block_height)

    if hasattr(args, 'balance_address'):
        get_balance(args.balance_address)

    if hasattr(args, 'blockchain_address'):
        create_blockchain(args.blockchain_address)

    if hasattr(args, 'send_from') and \
            hasattr(args, 'send_to') and \
            hasattr(args, 'send_amount'):
        send(args.send_from, args.send_to, args.send_amount)


# command
"""
python cli.py createwallet
python cli.py getbalance --address 1M2ZZAUWTzG6ocih4N2Yzr6D9B8bFj1XMy
python cli.py createblockchain --address 1X82i8GAzpSREp1pNLb6KzM9qZq1pjfbD 
python cli.py send --from 1X82i8GAzpSREp1pNLb6KzM9qZq1pjfbD --to 1M2ZZAUWTzG6ocih4N2Yzr6D9B8bFj1XMy --amount 6
python cli.py send --from 1JPHXxrL5kr849MHxkkQoeQGZ2ednqoMFy --to 1LzyZCn7QNNnKuafrdd7AtZVjnHQKzCmc8 --amount 4
"""
