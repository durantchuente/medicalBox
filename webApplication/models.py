import random
import string
from django.db import models
from django.contrib.auth.models import User

def generate_unique_code():
    # Génère un code de 5 chiffres aléatoires
    return ''.join(random.choices(string.digits, k=5))

# class User(models.Model):
#     id = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=255)
#     password = models.CharField(max_length=255)

class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    SEXE_CHOICES = [
        ('M', 'Homme'),
        ('F', 'Femme')
    ]
    gender = models.CharField(max_length=1, choices=SEXE_CHOICES)
    phoneNumber = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return (self.firstName + " "+ self.lastName)

class MedicalBox(models.Model):
    id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=50, unique=True)
    weight = models.FloatField(max_length=10)
    notes = models.TextField(blank=True, null=True)
    idPatient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    hours = models.ManyToManyField('HourMedication', related_name='boxes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return (self.address)

    # def save(self, *args, **kwargs):
    #     if not self.code:  # Générer un code uniquement si aucun n'est défini
    #         self.code = generate_unique_code()
    #     super(MedicalBox, self).save(*args, **kwargs)

class HourMedication(models.Model):
    name = models.CharField(max_length=100)
    time = models.TimeField()
    note = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class DataMedication(models.Model):
    id = models.AutoField(primary_key=True)
    weight = models.FloatField(max_length=10)
    TENDANCE_CHOICES = [
        ('H', 'High'),
        ('L', 'Low')
    ]
    tendance = models.CharField(max_length=1, choices=TENDANCE_CHOICES)
    DateTime = models.DateTimeField()
    medical_box = models.ForeignKey(MedicalBox, on_delete=models.CASCADE, related_name="related_entries")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"Poid du {self.DateTime} - Valeur: {self.weight}"
    