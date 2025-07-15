from django.urls import path
from .views import libro_diario

urlpatterns = [
    path('', libro_diario, name='libro_diario'),
]
