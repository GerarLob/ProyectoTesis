from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cliente
from .forms import ClienteForm
from bitacora.utils import registrar_accion
from usuarios.decorators import role_required  # 👈 Importar el decorador

@login_required
@role_required('admin', 'contador')
def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})

@login_required
@role_required('admin', 'contador')
def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            nuevo_cliente = form.save()
            registrar_accion(request.user, f"Registró al cliente {nuevo_cliente.nombres} {nuevo_cliente.apellidos}")
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'clientes/crear_cliente.html', {'form': form})

@login_required
@role_required('admin', 'contador')
def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    form = ClienteForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        registrar_accion(request.user, f"Editó al cliente {cliente.nombres} {cliente.apellidos}")
        return redirect('lista_clientes')
    return render(request, 'clientes/editar_cliente.html', {'form': form})

@login_required
@role_required('admin', 'contador')
def eliminar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        registrar_accion(request.user, f"Eliminó al cliente {cliente.nombres} {cliente.apellidos}")
        cliente.delete()
        return redirect('lista_clientes')
    return render(request, 'clientes/eliminar_cliente.html', {'cliente': cliente})
