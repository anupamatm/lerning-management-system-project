# student/urls.py

from django.urls import path
from .views import create_student

urlpatterns = [
    path('create/', create_student, name='create_student'),
]
