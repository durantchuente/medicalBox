from django import forms
from .models import MedicalBox, Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

class MedicalBoxForm(forms.ModelForm):
    class Meta:
        model = MedicalBox
        fields = '__all__'