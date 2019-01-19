from django import forms
from .models import Curso
class FormContacto(forms.Form):
    
    nombre = forms.CharField( max_length=120, widget=forms.TextInput(
        attrs={"id": "nombre", "class": "form-control form-control-lg form-control-a", "placeholder": "Ingrese nombre","data-rule":"minlen:4", "data-msg":"Please enter at least 4 chars"}))
    correo = forms.EmailField( max_length=30, widget=forms.EmailInput(
    	attrs={"id": "correo", "class": "form-control form-control-lg form-control-a", "placeholder": "direccioncorreo@correo.com","data-rule":"email", "data-msg":"Please enter a valid email"}))
    curso = forms.ModelChoiceField(queryset = Curso.objects.all(), empty_label = None, widget = forms.Select(attrs = { "id": "curso"}))
    mensaje = forms.CharField(required=True, widget=forms.Textarea(
    	attrs={"id": "mensaje", "class": "form-control", "placeholder": "Ingrese Mensaje","cols":"45", "rows":"8", "data-rule":"required", "data-msg":"Please write something for us"}))