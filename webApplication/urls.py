from django.urls import path
from .views import (
    CheckUserLoginStatus,
    DataMedicationListApiView,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('data', DataMedicationListApiView.as_view()),
    path('verifyAuth', CheckUserLoginStatus.as_view()),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]