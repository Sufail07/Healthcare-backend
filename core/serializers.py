from rest_framework import serializers
from .models import Patient, Doctor, PatientDoctorMapping
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

# A custom serializer for token obtaining (login), to allow logging in through email.
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'email'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'name', 'email', 'date_of_birth', 'address', 'phone_number', 'created_by']
        read_only_fields = ['created_by']
    
    # Ensuring email is unique
    def validate_email(self, value):
        queryset = Patient.objects.filter(email=value)
        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)

        if queryset.exists():
            raise serializers.ValidationError("Email already exists")
        return value
        
    
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'email', 'specialization', 'phone_number', 'consultation_fee']
        
    def validate_email(self, value):
        if Doctor.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value
    

    def create(self, validated_data):
        doctor = Doctor.objects.create(**validated_data)
        return doctor
    
    
class MappingSerializer(serializers.ModelSerializer):
    patient = serializers.SlugRelatedField(queryset=Patient.objects.all(), slug_field='name')
    doctor = serializers.SlugRelatedField(queryset=Doctor.objects.all(), slug_field='name')


    class Meta:
        model = PatientDoctorMapping
        fields = ['id', 'patient', 'doctor', 'mapped_at']

    # Ensuring that the patient and doctor that are already mapped, cannot be mapped again.
    def validate(self, data):
        patient = data.get('patient')
        doctor = data.get('doctor')

        if patient and doctor:
            queryset = PatientDoctorMapping.objects.filter(patient=patient, doctor=doctor)
            # During update, checking if there exists any other object with same patient and doctor. 
            if self.instance:
                queryset = queryset.exclude(pk=self.instance.pk)
            
            if queryset.exists():
                raise serializers.ValidationError('This patient is already mapped to this doctor')
            
        return data