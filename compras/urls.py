from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_compras, name='lista_compras'),
    path('crear/', views.crear_compra, name='crear_compra'),
    path('editar/<int:pk>/', views.editar_compra, name='editar_compra'),
    path('eliminar/<int:pk>/', views.eliminar_compra, name='eliminar_compra'),
]
