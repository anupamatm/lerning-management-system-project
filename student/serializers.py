# student/serializers.py

from rest_framework import serializers
from .models import Student
from authentication.models import CustomUser

class CreateStudentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Student
        fields = ['username', 'password', 'name', 'email', 'dob', 'date_of_joining', 'course_completed', 'joining_course', 'phone']

    def create(self, validated_data):
        user_data = {
            'username': validated_data.pop('username'),
            'password': validated_data.pop('password'),
            'email': validated_data['email'],
            'user_type': 'student'
        }
        user = CustomUser.objects.create_user(**user_data)
        student = Student.objects.create(user=user, **validated_data)
        return student
