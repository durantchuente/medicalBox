from rest_framework import serializers
from .models import DataMedication
class DataMedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataMedication
        fields = '__all__'