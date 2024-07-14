from django.shortcuts import render, redirect
from med.models import Patient

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
		return redirect('patient-profile')
	else:
		return render(request, 'patient_reg.html')
