from django.urls import path
from .views import libro_diario
from .views import libro_diario, libro_mayor

urlpatterns = [
    path('', libro_diario, name='libro_diario'),
    path('mayor/', libro_mayor, name='libro_mayor')
]
