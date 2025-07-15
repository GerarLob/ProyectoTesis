from django.db import models
from clientes.models import Cliente

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateField()
    descripcion = models.CharField(max_length=255)
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Venta a {self.cliente.nombres} {self.cliente.apellidos} - {self.fecha}"
