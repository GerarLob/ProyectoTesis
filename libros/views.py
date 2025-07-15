from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from usuarios.decorators import role_required
from .models import AsientoDiario

@login_required
@role_required('admin', 'contador')
def libro_diario(request):
    asientos = AsientoDiario.objects.all().order_by('fecha')
    return render(request, 'libros/libro_diario.html', {'asientos': asientos})
from django.shortcuts import render

# Create your views here.
