# teacher/models.py

from django.db import models
from authentication.models import CustomUser

class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dob = models.DateField()  # Date of birth
    phone = models.CharField(max_length=15)  # Phone number
    email_id = models.EmailField()

    def __str__(self):
        return self.user.username
