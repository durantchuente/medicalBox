from datetime import datetime
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from webApplication.forms import HourMedicationForm, MedicalBoxForm, PatientForm
from webApplication.models import DataMedication, HourMedication, MedicalBox, Patient, User
from webApplication.permissions import IsAdminAuthenticated
from .serializers import DataMedicationSerializer
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import handle_db_permission_error

class DataMedicationListApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    permission_classes = [IsAdminAuthenticated]
    # 1. List all
    @login_required
    def get(self, request, *args, **kwargs):
        '''
        List all the data items for box medication
        '''
        datas = DataMedication.objects.all()
        serializer = DataMedicationSerializer(datas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    # @login_required
    permission_classes = [IsAdminAuthenticated]
    def post(self, request, *args, **kwargs):
        '''
        Create the Data Medication
        '''
        address = request.data.get('address')
        data = {
            "weight": request.data.get('weight'),
            "tendance": request.data.get('tendance'),
            "DateTime": datetime.now().isoformat(),
            "medical_box": get_object_or_404(MedicalBox, address=address).id,
            "user": request.user.id
        }
        # print(get_object_or_404(MedicalBox, address=address).__dict__)
        serializer = DataMedicationSerializer(data=data)
        serializer = DataMedicationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CheckUserLoginStatus(APIView):
    def get(self, request):
        # Vérifie si l'utilisateur est authentifié
        is_authenticated = request.user.is_authenticated
        # Renvoie true si l'utilisateur est authentifié, false sinon
        return Response({"data": is_authenticated})

@handle_db_permission_error
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Connexion réussie !")
            return redirect('patient')  # Redirigez vers la page d'accueil après connexion
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
    return render(request, 'login.html')  # Template pour la page de connexion

def user_logout(request):
    logout(request)
    messages.info(request, "Déconnexion réussie.")
    return redirect('login')  # Redirigez vers la page de connexion après déconnexion

@login_required
@handle_db_permission_error
def data(request):
    return render(request, 'data.html')

@login_required
@handle_db_permission_error
def chart(request):
    # datas = DataMedication.objects.filter(user=request.user)
    datas = DataMedication.objects.all()
    weights = [data.weight for data in datas]
    dates = [data.DateTime.strftime('%Y-%m-%d %H:%M:%S') for data in datas]
    return render(request, 'chart.html', {'weights': weights, 'dates': dates})

def get_data(request):
    # datas = DataMedication.objects.filter(user=request.user).values('weight', 'tendance', 'DateTime', 'medical_box__address')
    datas = DataMedication.objects.all().values('weight', 'tendance', 'DateTime', 'medical_box__address')
    data_list = list(datas)  # Convertir la QuerySet en une liste de dictionnaires
    # serializer = DataMedicationSerializer(data_list, many=True)
    return JsonResponse({'data': data_list})

@login_required
@handle_db_permission_error
def patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.user = request.user
            patient.save()
            return redirect('patient')
        else:
            print(form.errors)
    else:
        form = PatientForm()
    # patients = Patient.objects.filter(user=request.user)
    patients = Patient.objects.all()
    return render(request, 'patient.html', {'form': form, 'patients': patients})

@login_required
@handle_db_permission_error
def hourMedication(request):
    if request.method == 'POST':
        form = HourMedicationForm(request.POST)
        if form.is_valid():
            hourM = form.save(commit=False)
            hourM.user = request.user
            hourM.save()
            return redirect('hourMedication')
        else:
            print(form.errors)
    else:
        form = HourMedicationForm()
    # hours = HourMedication.objects.filter(user=request.user)
    hours = HourMedication.objects.all()
    return render(request, 'hourMedication.html', {'form': form, 'hours': hours})

@login_required
@handle_db_permission_error
def medicalBox(request):
    if request.method == 'POST':
        form = MedicalBoxForm(request.POST)
        if form.is_valid():
            hours_ids = request.POST.getlist('hours')
            box_medication = form.save(commit=False)
            box_medication.user = request.user
            box_medication.save()
            hours_selected = HourMedication.objects.filter(id__in=hours_ids)
            box_medication.hours.set(hours_selected)
            # form.save()
            return redirect('medicalBox')
        else:
            print(form.errors)
    else:
        form = MedicalBoxForm()
    # boxes = MedicalBox.objects.filter(user=request.user)
    # patients = Patient.objects.filter(user=request.user)
    # hours = HourMedication.objects.filter(user=request.user)
    boxes = MedicalBox.objects.all()
    patients = Patient.objects.all()
    hours = HourMedication.objects.all()
    for box in boxes:
        hours = box.hours.all()  # Récupérer toutes les heures associées
        print(f"Box: {box.address}, Hours: {[hour.time.strftime('%H:%M') for hour in hours]}")
    return render(request, 'boxMedicament.html', {'form': form, 'boxes': boxes, 'patients': patients, 'hours': hours})
