from django import forms
from .models import Mascota

class FormularioRegistro(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['Nombre', 'Especie', 'Raza', 'Edad', 'Dueno', 'Telefono', 'Foto']
        widgets = {
            'Nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la mascota'}),
            'Especie': forms.Select(attrs={'class': 'form-select'}),
            'Raza': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Raza'}),
            'Edad': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Edad en años'}),
            'Dueno': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del dueño'}),
            'Telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono de contacto'}),
            'Foto': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'Nombre': 'Nombre',
            'Especie': 'Especie',
            'Raza': 'Raza',
            'Edad': 'Edad',
            'Dueno': 'Dueño',
            'Telefono': 'Teléfono',
            'Foto': 'Foto de la mascota',
        }
