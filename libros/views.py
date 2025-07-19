from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from usuarios.decorators import role_required
from .models import AsientoDiario

from decimal import Decimal
from django.db.models import Sum, DecimalField
from django.db.models.functions import Coalesce

# 📘 Libro Mayor
@login_required
@role_required('admin', 'contador')
def libro_mayor(request):
    cuentas = (
        AsientoDiario.objects
        .values('cuenta')
        .annotate(
            total_debe=Coalesce(Sum('debe'), Decimal('0.00'), output_field=DecimalField()),
            total_haber=Coalesce(Sum('haber'), Decimal('0.00'), output_field=DecimalField())
        )
        .order_by('cuenta')
    )

    for cuenta in cuentas:
        saldo = cuenta['total_debe'] - cuenta['total_haber']
        cuenta['saldo'] = saldo
        cuenta['saldo_abs'] = abs(saldo)  # Para evitar el filtro no soportado en la plantilla

    return render(request, 'libros/libro_mayor.html', {'cuentas': cuentas})

# 📕 Libro Diario
@login_required
@role_required('admin', 'contador')
def libro_diario(request):
    asientos = AsientoDiario.objects.all().order_by('fecha')
    return render(request, 'libros/libro_diario.html', {'asientos': asientos})
