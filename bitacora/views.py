from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from usuarios.decorators import role_required
from .models import Bitacora

@login_required
@role_required('admin')  # solo el admin puede ver la bitácora
def ver_bitacora(request):
    registros = Bitacora.objects.all().order_by('-fecha')
    return render(request, 'bitacora/ver_bitacora.html', {'registros': registros})
