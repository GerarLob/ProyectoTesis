from django.db import models
from django.conf import settings

class Bitacora(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    accion = models.CharField(max_length=255)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.accion} - {self.fecha.strftime('%d/%m/%Y %H:%M')}"
