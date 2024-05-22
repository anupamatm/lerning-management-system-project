# teacher/urls.py

from django.urls import path
from .views import create_teacher

urlpatterns = [
    path('create_teacher/', create_teacher, name='create_teacher'),
]
