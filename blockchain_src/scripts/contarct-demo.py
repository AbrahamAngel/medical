from web3 import Web3

import json

# Path to your contract's ABI JSON file
abi_path = './build/contracts/demo.json'

# Load the ABI from the JSON file
with open(abi_path, 'r') as file:
    contract_json = json.load(file)
    contract_abi = contract_json['abi']

print(contract_abi)


# Connect to the local Ganache instance
w3 = Web3(Web3.HTTPProvider('http://localhost:7545'))

# Check if we're connected to the network
if not w3.is_connected():
    print("Failed to connect to the Ethereum client")
    exit(1)

# The ABI of your contract
contract_abi = contract_abi

# The address of your deployed contract
contract_address = "0x4Ae5f0EbfD6c1835267Fd5F0aC9aAFFe51D362e6"

# Create a contract object
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Call a function of the contract
# Replace 'myFunction' with the name of the function you want to call,
# and adjust the parameters accordingly.
result = contract.functions.myFunction().call()

print(f"Result of calling myFunction: {result}")
