from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Administrador'),
        ('contador', 'Contador'),
        ('auxiliar', 'Auxiliar Contable'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='contador')

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
