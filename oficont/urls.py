from django.contrib import admin
from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include('clientes.urls')),
    path('', include('usuarios.urls')),
    path('bitacora/', include('bitacora.urls')),
    path('ventas/', include('ventas.urls')),
    path('compras/', include('compras.urls')),
    path('libros/', include('libros.urls')),

]
