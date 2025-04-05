from django.contrib.auth.models import AbstractUser
from django.db import models

class Users(AbstractUser):
    account_id = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True
    )

    role_choices = [
        ('resident', 'Resident'),
        ('meter_reader', 'Meter Reader'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(max_length=20, choices=role_choices, default='resident')

    def __str__(self):
        return self.username
