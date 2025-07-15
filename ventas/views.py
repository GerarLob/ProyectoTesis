from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Venta
from .forms import VentaForm
from bitacora.utils import registrar_accion
from usuarios.decorators import role_required

@login_required
@role_required('admin', 'contador')
def lista_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'ventas/lista_ventas.html', {'ventas': ventas})

@login_required
@role_required('admin', 'contador')
def crear_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            venta = form.save()
            registrar_accion(request.user, f"Registró venta: {venta.descripcion} por Q{venta.monto}")
            return redirect('lista_ventas')
    else:
        form = VentaForm()
    return render(request, 'ventas/crear_venta.html', {'form': form})

@login_required
@role_required('admin', 'contador')
def editar_venta(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    form = VentaForm(request.POST or None, instance=venta)
    if form.is_valid():
        form.save()
        registrar_accion(request.user, f"Editó venta: {venta.descripcion}")
        return redirect('lista_ventas')
    return render(request, 'ventas/editar_venta.html', {'form': form})

@login_required
@role_required('admin', 'contador')
def eliminar_venta(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        registrar_accion(request.user, f"Eliminó venta: {venta.descripcion}")
        venta.delete()
        return redirect('lista_ventas')
    return render(request, 'ventas/eliminar_venta.html', {'venta': venta})
