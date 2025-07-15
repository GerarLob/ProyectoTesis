from .models import AsientoDiario
from datetime import date

def registrar_asiento(fecha: date, descripcion: str, cuenta: str, debe: float, haber: float):
    AsientoDiario.objects.create(
        fecha=fecha,
        descripcion=descripcion,
        cuenta=cuenta,
        debe=debe,
        haber=haber
    )
