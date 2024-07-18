from web3 import Web3
import json

# Path to your contract's ABI JSON file
# abi_path = './build/contracts/Appointment.json'

# # Load the ABI from the JSON file
# with open(abi_path, 'r') as file:
#     contract_json = json.load(file)
#     contract_abi = contract_json['abi']

# print(contract_abi)

def interact_with_appointment_contract(contract_address, contract_abi, name, gender, age):
    """
    Interacts with the Appointment contract by creating an appointment and retrieving it.

    :param contract_address: The address of the deployed Appointment contract.
    :param contract_abi: The ABI of the Appointment contract.
    """
    # Initialize a Web3 instance connected to Ganache
    w3 = Web3(Web3.HTTPProvider('http://localhost:7545'))

    # Check if we're connected to the network
    if not w3.is_connected():
        print("Failed to connect to the Ethereum client")
        return

    # Create a contract object
    contract = w3.eth.contract(address=contract_address, abi=contract_abi)

    # Specify the account you're using to send the transaction
    account = w3.eth.accounts[0]  # Using the first available account

    # Details for the new appointment
    patientName = name
    doctorName = gender
    appointmentDate = int(age)

    # Estimate gas required for the transaction
    tx_hash = contract.functions.createAppointment(patientName, doctorName, appointmentDate).estimate_gas({
        'from': account
    })
    print(tx_hash)

    # Send the transaction
    tx_receipt = contract.functions.createAppointment(patientName, doctorName, appointmentDate).transact({
        'from': account, 'gas': tx_hash
    })

    print(f"Transaction Hash: {tx_receipt.hex()}")

    # Wait for the transaction to be mined and get the transaction receipt
    receipt = w3.eth.wait_for_transaction_receipt(tx_receipt)
    print(f"Transaction Receipt: {receipt}")

    # Retrieve and print the appointments made by the caller
    appointments = contract.functions.getAppointments().call()
    print(f"Appointments made by {account}:")
    print(appointments)
    for appointment in appointments:
        print(f"- Patient Name: {appointment.patientName}, Doctor Name: {appointment.doctorName}, Appointment Date: {appointment.appointmentDate}")

        

# # Example usage
# if __name__ == "__main__":

#     contract_address = "0xda5479737d7d6384a4a5e5e1afD60EBD3B9bDd13"  # Replace with your contract's address
#     contract_abi = contract_abi  # Replace with your contract's ABI
#     interact_with_appointment_contract(contract_address, contract_abi)
