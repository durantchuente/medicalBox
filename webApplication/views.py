from django.shortcuts import redirect, render

from webApplication.forms import MedicalBoxForm, PatientForm
from webApplication.models import MedicalBox, Patient

def patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient')
        else:
            print(form.errors)
    else:
        form = PatientForm()
    patients = Patient.objects.all()
    return render(request, 'patient.html', {'form': form, 'patients': patients})

def medicalBox(request):
    if request.method == 'POST':
        form = MedicalBoxForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medicalBox')
        else:
            print(form.errors)
    else:
        form = MedicalBoxForm()
    boxes = MedicalBox.objects.all()
    patients = Patient.objects.all()
    return render(request, 'boxMedicament.html', {'form': form, 'boxes': boxes, 'patients': patients})
