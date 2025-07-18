from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label="Usuario", widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Correo o nombre de usuario'
    }))
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Contraseña'
    }))
