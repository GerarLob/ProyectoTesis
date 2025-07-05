from .models import Bitacora

def registrar_accion(usuario, accion):
    Bitacora.objects.create(usuario=usuario, accion=accion)
