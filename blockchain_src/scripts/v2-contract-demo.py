from web3 import Web3
import json

# Path to your contract's ABI JSON file
abi_path = './build/contracts/demo.json'

# Load the ABI from the JSON file
with open(abi_path, 'r') as file:
    contract_json = json.load(file)
    contract_abi = contract_json['abi']

print(contract_abi)

# Assuming you've already set up your Web3 connection and loaded the ABI and address
w3 = Web3(Web3.HTTPProvider('http://localhost:7545'))
contract_address = "0x414F236641ADc591C41cE93537F10B701feDEd2c"
contract_abi = contract_abi
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Specify the account you're using to send the transaction
account = w3.eth.accounts[0]

# The value you want to set
new_number = 34567 #request.POST.get('new_num')

# Estimate gas required for the transaction
tx_hash = contract.functions.set(new_number).estimate_gas({'from': account})
print(tx_hash)
# Send the transaction
tx_receipt = contract.functions.set(new_number).transact({'from': account, 'gas': tx_hash})
print(tx_receipt)
print(f"Transaction Hash: {tx_receipt.hex()}")

receipt = w3.eth.wait_for_transaction_receipt(tx_receipt)
print(f"Transaction Receipt: {receipt}")

# Call the 'get' function of the contract to retrieve the current value of 'number'
current_number = contract.functions.get().call()

# Print the current value of 'number'
print(f"The current value of 'number' is: {current_number}")