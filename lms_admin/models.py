# lms_admin/models.py

from django.db import models
from authentication.models import CustomUser

class LmsAdmin(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    username = models.CharField(max_length=255, default='')
    password = models.CharField(max_length=255, default='')
    # Add additional fields specific to admin if needed

    def save(self, *args, **kwargs):
        # Ensure that the password is hashed before saving
        self.user.set_password(self.password)
        self.user.save()
        super().save(*args, **kwargs)
