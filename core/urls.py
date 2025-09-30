from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import CustomTokenObtainPairView, RegisterView, DoctorViewSet, PatientViewSet, mapping_view
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'patients', PatientViewSet, basename='patient') 
router.register(r'doctors', DoctorViewSet, basename='doctor') 


urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register_user'),
    path('auth/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('mappings/', mapping_view, name='all_mapping'),
    path('mappings/<int:patient_id>/', mapping_view, name='mapping_patient'),
    path('mappings/<int:id>', mapping_view, name='mapping_patient'),
]

urlpatterns += router.urls