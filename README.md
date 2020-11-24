

# b07502072BTC


Source from [blockchain-py](https://github.com/yummybian/blockchain-py)


## Prerequisites
### Install [pipenv](https://github.com/pypa/pipenv)

### Install this project's dependencies
```bash
pipenv install
```

### Activate this project's virtualenv
```bash
pipenv shell
```

### Go to the directory
```bash
$ cd blockchain-py
```

## How to use
### Create a wallet
```bash
$ python cli.py createwallet
Your new address: 17Y288D5DnFwU6cj5M8YHnxYNnDhN6f5FK
```

### Create blockchain and receive first mining reward
```bash
$ python cli.py createblockchain --address 17Y288D5DnFwU6cj5M8YHnxYNnDhN6f5FK
```

### Create another wallet
```bash
$ python cli.py createwallet
Your new address: 15zBUPbr2B4JMcQHg6oJ8DYQi4t7RN1gWb
```

### Send coins to someone
```bash
$ python cli.py send --from 17Y288D5DnFwU6cj5M8YHnxYNnDhN6f5FK --to 15zBUPbr2B4JMcQHg6oJ8DYQi4t7RN1gWb --amount 6
Mining a new block
0005ec56906edfcc97a8b422cd6948e7a2b59cba89e9a253f75eeefb6755d6e9


Success!
```

### Get balance of some address
```bash
$ python cli.py getbalance --address 17Y288D5DnFwU6cj5M8YHnxYNnDhN6f5FK 
Balance of 17Y288D5DnFwU6cj5M8YHnxYNnDhN6f5FK:
```

### Print out the whole blockchain
```bash
$ python cli.py printchain
Prev. hash: 003971542065a0200022725bed2bd612b35495d4121f2359a0ef20fa07364953
Hash: 00116a06cb01eea5b90e7b686244c5a369956adb6daf2d55e68c5d510864bcf9
Height: 2
PoW: True
Prev. hash:
Hash: 003971542065a0200022725bed2bd612b35495d4121f2359a0ef20fa07364953
Height: 1
PoW: True
```

### Print out one of the block (assigned by height)
```bash
$ python cli.py printblock --height 2
Prev. hash: 003971542065a0200022725bed2bd612b35495d4121f2359a0ef20fa07364953
Hash: 00116a06cb01eea5b90e7b686244c5a369956adb6daf2d55e68c5d510864bcf9
Height: 2
PoW: True
```

## Functionalities

**Todos**
- [x] [Prototype]         Block(10%), Blockchain(10%), Proof-of-Work(20%) 40%
- [x] [Persistence]       Database(20%), Client(20%)                      40%
- [x] [Transactionbasic]  UTXO(5%) or Account model(2%)                   5%
- [x] [Address]           Sign & Verify(5%)                               5%
- [x] [Transaction]       Mining reward(2%), Merkle tree(8%)              10%
- [ ] [Network]           P2P(10%) or Server-Client(7%)                   10%
