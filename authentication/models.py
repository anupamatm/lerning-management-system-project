# authentication/models.py

from django.contrib.auth.models import AbstractUser, Group, Permission, BaseUserManager
from django.db import models

# Custom manager for CustomUser
class CustomUserManager(BaseUserManager):
    """
    Custom user manager for handling the creation of users and superusers.
    """

    def create_user(self, username, email=None, password=None, **extra_fields):
        """
        Creates and saves a regular user with the given username, email, and password.
        """
        if not username:
            raise ValueError('The Username field must be set')
        
        # Normalize the email address
        email = self.normalize_email(email)
        
        # Create a new user instance
        user = self.model(username=username, email=email, **extra_fields)
        
        # Set the user's password (hashed)
        user.set_password(password)
        
        # Save the user to the database
        user.save(using=self._db)
        
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given username, email, and password.
        """
        # Set default fields for superuser
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('user_type', 'admin')

        # Ensure the superuser has the correct permissions
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        # Use the create_user method to create the superuser
        return self.create_user(username, email, password, **extra_fields)

# Custom user model extending AbstractUser
class CustomUser(AbstractUser):
    """
    Custom user model that extends the default Django AbstractUser model.
    Adds a user_type field to differentiate between admin, student, and teacher.
    """
    
    # Choices for the user_type field
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    )
    
    # Additional field to store the user type
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    
    # Use the custom user manager
    objects = CustomUserManager()

    # Override the default groups relationship to avoid conflicts
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Custom related name to avoid conflicts
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='custom_user'
    )
    
    # Override the default user_permissions relationship to avoid conflicts
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_set',  # Custom related name to avoid conflicts
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='custom_user'
    )

    def __str__(self):
        """
        String representation of the CustomUser model.
        """
        return self.username
