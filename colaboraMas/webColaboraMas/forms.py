from django import forms
from .models import Curso
class FormContacto(forms.Form):
    
    nombre = forms.CharField(label="Nombre completo", max_length=120, widget=forms.TextInput(
        attrs={"id": "nombre", "class": "form-control", "placeholder": "Ingrese nombre"}))
    correo = forms.EmailField(label="Correo electrónico", max_length=30, widget=forms.EmailInput(
    	attrs={"id": "correo", "class": "form-control", "placeholder": "direccioncorreo@correo.com"}))
    curso = forms.ModelChoiceField(label = "Curso", queryset = Curso.objects.all(), empty_label = None, widget = forms.Select(attrs = { "id": "curso"}))
    mensaje = forms.CharField(label="Mensaje", required=True, widget=forms.TextInput(
    	attrs={"id": "mensaje", "class": "form-control", "placeholder": "Ingrese Mensaje"}))