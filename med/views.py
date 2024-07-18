from django.shortcuts import render, redirect
from med.models import Patient
from med.utils import interact_with_appointment_contract
import json

def index(request):
	return render(request, 'index.html')

def patient_profile(request):
	patient = Patient.objects.all()
	print(patient)
	context = {'patient': patient}
	return render(request, 'patient_profile.html', context)

def patient_reg(request):
	if request.method=="POST":
		name=request.POST.get("name")
		age=request.POST.get("age")
		gender=request.POST.get("gender")
		bloodgroup=request.POST.get("bloodgroup")
		allergies=request.POST.get("allergies")

		Patient.objects.create(	
			name=name,
			age=age,
			gender=gender,
			bloodgroup=bloodgroup,
			allergies=allergies,
		)
		abi_path = './blockchain_src/build/contracts/Appointment.json'

		# Load the ABI from the JSON file
		with open(abi_path, 'r') as file:
			contract_json = json.load(file)
			contract_abi = contract_json['abi']
			contract_address = "0xda5479737d7d6384a4a5e5e1afD60EBD3B9bDd13"  # Replace with your contract's address


		print(contract_abi)
		interact_with_appointment_contract(contract_address, contract_abi, name, gender, age)
		return redirect('patient-profile')

	return render(request, 'patient_reg.html')

