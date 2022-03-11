from rest_framework import serializers
from DrivingSchool.models import *

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = instructor
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = '__all__'

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = schedule
        fields = '__all__'

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = enrollment
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = payment
        fields = '__all__'