from datetime import datetime
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from webApplication.forms import HourMedicationForm, MedicalBoxForm, PatientForm
from webApplication.models import DataMedication, HourMedication, MedicalBox, Patient
from .serializers import DataMedicationSerializer

class DataMedicationListApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the data items for box medication
        '''
        datas = DataMedication.objects.all()
        datas = DataMedication.objects.filter(id = request.data.id)
        serializer = DataMedicationSerializer(datas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Data Medication
        '''
        address = request.data.get('address')
        data = {
            "weight": request.data.get('weight'), 
            "tendance": request.data.get('tendance'), 
            "DateTime": datetime.now(),
            "medical_box": get_object_or_404(MedicalBox, address=address).id
        }
        print(get_object_or_404(MedicalBox, address=address).__dict__)
        serializer = DataMedicationSerializer(data=data)
        # serializer = DataMedicationSerializer(data=data)
        if serializer.is_valid():
            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def data(request):
    datas = DataMedication.objects.all()
    return render(request, 'data.html', {'datas': datas})

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
