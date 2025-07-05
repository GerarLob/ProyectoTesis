from django.db import models

class Cliente(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    nit = models.CharField(max_length=20, unique=True)
    agencia_virtual = models.CharField(max_length=100, blank=True, null=True)
    celular = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos} - NIT: {self.nit}"
