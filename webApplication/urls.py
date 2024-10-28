from django.urls import path
from .views import (
    DataMedicationListApiView,
)

urlpatterns = [
    path('api/data', DataMedicationListApiView.as_view()),
]