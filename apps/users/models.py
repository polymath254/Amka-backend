from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    # Extend as needed for AMKA profile fields
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    is_approved = models.BooleanField(default=False)  # For admin approval flow
    bio = models.TextField(blank=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username or self.email

