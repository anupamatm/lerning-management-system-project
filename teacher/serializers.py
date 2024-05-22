# teacher/serializers.py

from rest_framework import serializers
from authentication.models import CustomUser
from .models import Teacher

class CreateTeacherSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.email')
    password = serializers.CharField(write_only=True)
    user_type = serializers.CharField(source='user.user_type', default='teacher', read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    dob = serializers.DateField()
    phone = serializers.CharField()
    email_id = serializers.EmailField()

    class Meta:
        model = Teacher
        fields = ['username', 'email', 'password', 'user_type', 'first_name', 'last_name', 'dob', 'phone', 'email_id']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        password = validated_data.pop('password')
        user = CustomUser.objects.create_user(**user_data, password=password, user_type='teacher')
        teacher = Teacher.objects.create(user=user, **validated_data)
        return teacher
