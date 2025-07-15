from django.urls import path
from .views import ver_bitacora

urlpatterns = [
    path('', ver_bitacora, name='ver_bitacora'),
]
