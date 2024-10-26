from django.shortcuts import redirect, render

from webApplication.forms import HourMedicationForm, MedicalBoxForm, PatientForm
from webApplication.models import HourMedication, MedicalBox, Patient

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

def hourMedication(request):
    if request.method == 'POST':
        form = HourMedicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hourMedication')
        else:
            print(form.errors)
    else:
        form = HourMedicationForm()
    hours = HourMedication.objects.all()
    return render(request, 'hourMedication.html', {'form': form, 'hours': hours})

def medicalBox(request):
    if request.method == 'POST':
        form = MedicalBoxForm(request.POST)
        if form.is_valid():
            hours_ids = request.POST.getlist('hours')
            box_medication = form.save(commit=False)
            box_medication.save()
            hours_selected = HourMedication.objects.filter(id__in=hours_ids)
            box_medication.hours.set(hours_selected)
            # form.save()
            return redirect('medicalBox')
        else:
            print(form.errors)
    else:
        form = MedicalBoxForm()
    boxes = MedicalBox.objects.all()
    patients = Patient.objects.all()
    hours = HourMedication.objects.all()
    for box in boxes:
        hours = box.hours.all()  # Récupérer toutes les heures associées
        print(f"Box: {box.address}, Hours: {[hour.time.strftime('%H:%M') for hour in hours]}")
    return render(request, 'boxMedicament.html', {'form': form, 'boxes': boxes, 'patients': patients, 'hours': hours})
