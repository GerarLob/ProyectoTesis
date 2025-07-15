from django.db import models
from django.utils import timezone

class AsientoDiario(models.Model):
    fecha = models.DateField(default=timezone.now)
    descripcion = models.TextField()
    cuenta = models.CharField(max_length=100)
    debe = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    haber = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.fecha} | {self.descripcion} | {self.cuenta} | D: {self.debe} / H: {self.haber}"
