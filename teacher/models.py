from django.db import models

from authentication.models import CustomUser

# Create your models here.
# authentication/models.py

class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    # Add additional fields specific to teacher if needed
