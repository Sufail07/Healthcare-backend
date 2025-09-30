from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .serializers import PatientSerializer, DoctorSerializer, UserRegistrationSerializer, CustomTokenObtainPairSerializer, MappingSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Patient, PatientDoctorMapping, Doctor
from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions


# Create your views here.


class RegisterView(CreateAPIView):
    serializer_class = UserRegistrationSerializer

# Custom login view to accept email for logging in
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

'''
CRUD for patients. User can only see the patients that they have created.
'''
class PatientViewSet(ModelViewSet):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Patient.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        

'''
CRUD for Doctors.
'''
class DoctorViewSet(ModelViewSet):
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Doctor.objects.all()
    

'''
Endpoints to create, view and delete patient-doctor mappings.
'''
@api_view(['POST', 'GET', 'DELETE'])
@permission_classes([permissions.IsAuthenticated])
def mapping_view(request, patient_id=None, id=None):
    if request.method == 'POST':
        serializer = MappingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        # Retriving the details of doctors assigned to a specific patient, if patient_id is provided.
        if patient_id:
            queryset = PatientDoctorMapping.objects.filter(patient_id=patient_id).select_related('doctor')
            if not queryset.exists():
                return Response({'error': 'No mappings found for the patient'}, status=status.HTTP_404_NOT_FOUND)
            
            doctors = [m.doctor for m in queryset]
            serializer = DoctorSerializer(doctors, many=True)
            
        else:
            queryset = PatientDoctorMapping.objects.all()
            serializer = MappingSerializer(queryset, many=True)
            
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        if not id:
            return Response({'error': 'Mapping ID not provided'}, status=status.HTTP_400_BAD_REQUEST)
        
        mapping = get_object_or_404(PatientDoctorMapping, id=id)
        mapping.delete()
        return Response({'message': 'Mapping object successfully deleted'}, status=status.HTTP_204_NO_CONTENT)

        
        