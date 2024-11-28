from django import forms
from .models import DataMedication, HourMedication, MedicalBox, Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['firstName', 'lastName', 'gender', 'phoneNumber', 'email']

class MedicalBoxForm(forms.ModelForm):
    class Meta:
        model = MedicalBox
        fields = ['address', 'weight', 'notes', 'idPatient', 'hours']

class HourMedicationForm(forms.ModelForm):
    class Meta:
        model = HourMedication
        fields = ['name', 'time', 'note']

class DataMedicationForm(forms.ModelForm):
    class Meta:
        model = DataMedication
        fields = ['weight', 'tendance']