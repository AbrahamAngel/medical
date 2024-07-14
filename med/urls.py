from django.urls import path
from med.views import index, patient_reg, patient_profile

urlpatterns = [
    path('index/', index, name='index'),
    path('patient-reg/', patient_reg, name='patients-reg'),
    path('patient-profile/', patient_profile, name='patient-profile')
]

