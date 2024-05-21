# authentication/urls.py

from django.urls import path
from .views import admin_login, student_login, teacher_login, profile

urlpatterns = [
    path('lmsadmin/login/', admin_login, name='admin_login'),
    path('student/login/', student_login, name='student_login'),
    path('teacher/login/', teacher_login, name='teacher_login'),
    path('profile/', profile, name='profile'),
]
