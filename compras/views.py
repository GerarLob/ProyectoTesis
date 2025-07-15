from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Compra
from .forms import CompraForm
from bitacora.utils import registrar_accion
from usuarios.decorators import role_required
from libros.utils import registrar_asiento


@login_required
@role_required('admin', 'contador')
def lista_compras(request):
    compras = Compra.objects.all()
    return render(request, 'compras/lista_compras.html', {'compras': compras})

@login_required
@role_required('admin', 'contador')
def crear_compra(request):
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            compra = form.save()
            registrar_accion(request.user, f"Registró compra: {compra.descripcion} por Q{compra.monto}")
            registrar_asiento(
                fecha=compra.fecha,
                descripcion=f"Compra a {compra.proveedor}",
                cuenta="Compras",
                debe=compra.monto,
                haber=0
            )
            return redirect('lista_compras')
    else:
        form = CompraForm()
    return render(request, 'compras/crear_compra.html', {'form': form})

@login_required
@role_required('admin', 'contador')
def editar_compra(request, pk):
    compra = get_object_or_404(Compra, pk=pk)
    form = CompraForm(request.POST or None, instance=compra)
    if form.is_valid():
        form.save()
        registrar_accion(request.user, f"Editó compra: {compra.descripcion}")
        return redirect('lista_compras')
    return render(request, 'compras/editar_compra.html', {'form': form})

@login_required
@role_required('admin', 'contador')
def eliminar_compra(request, pk):
    compra = get_object_or_404(Compra, pk=pk)
    if request.method == 'POST':
        registrar_accion(request.user, f"Eliminó compra: {compra.descripcion}")
        compra.delete()
        return redirect('lista_compras')
    return render(request, 'compras/eliminar_compra.html', {'compra': compra})
