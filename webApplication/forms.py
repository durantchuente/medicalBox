from django import forms
from .models import HourMedication, MedicalBox, Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

class MedicalBoxForm(forms.ModelForm):
    class Meta:
        model = MedicalBox
        fields = '__all__'

class HourMedicationForm(forms.ModelForm):
    class Meta:
        model = HourMedication
        fields = '__all__'