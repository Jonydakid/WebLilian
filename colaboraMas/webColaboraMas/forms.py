from django import forms
from .models import Curso
class FormContacto(forms.Form):
    
    nombre = forms.CharField(label="Nombre completo", max_length=120, widget=forms.TextInput(
        attrs={"id": "nombre", "class": "campo", "placeholder": "Ingrese nombres"}))
    correo = forms.EmailField(label="Correo electrónico", max_length=30, widget=forms.EmailInput(
    	attrs={"id": "correo", "class": "campo", "placeholder": "direccioncorreo@correo.com"}))
    curso = forms.ModelChoiceField(label = "Curso", queryset = Curso.objects.all(), empty_label = None, widget = forms.Select(attrs = { "id": "curso"}))
    mensaje = forms.CharField(label="Mensaje", required=True, widget=forms.TextInput(
    	attrs={"id": "mensaje", "class": "campo", "placeholder": "Ingrese Mensaje"}))