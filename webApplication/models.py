import random
import string
from django.db import models

def generate_unique_code():
    # Génère un code de 5 chiffres aléatoires
    return ''.join(random.choices(string.digits, k=5))

class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    SEXE_CHOICES = [
        ('M', 'Homme'),
        ('F', 'Femme')
    ]
    gender = models.CharField(max_length=1, choices=SEXE_CHOICES)
    phoneNumber = models.IntegerField()
    email = models.EmailField()
    def __str__(self):
        return (self.firstName + " "+ self.lastName)

class MedicalBox(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=5, unique=True, blank=True)
    weight = models.CharField(max_length=255)
    notes = models.TextField(blank=True, null=True)
    idPatient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.code:  # Générer un code uniquement si aucun n'est défini
            self.code = generate_unique_code()
        super(MedicalBox, self).save(*args, **kwargs)
