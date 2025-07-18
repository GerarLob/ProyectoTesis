from django.urls import path
from .views import CustomLoginView, bienvenida
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', bienvenida, name='bienvenida'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
