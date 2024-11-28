from django.contrib import admin
from webApplication.models import Patient, MedicalBox, HourMedication, DataMedication

admin.site.register([Patient, MedicalBox, HourMedication, DataMedication])