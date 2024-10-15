from django.contrib import admin
from webApplication.models import Patient, MedicalBox

admin.site.register([Patient, MedicalBox])