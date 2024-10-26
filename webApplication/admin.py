from django.contrib import admin
from webApplication.models import Patient, MedicalBox, HourMedication

admin.site.register([Patient, MedicalBox, HourMedication])