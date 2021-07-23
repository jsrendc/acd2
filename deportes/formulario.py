from django import forms
from .models import Deporte


class FormularioArte(forms.ModelForm):
    
    class Meta:
        model = Deporte
        fields=["nombre","descripcion"]