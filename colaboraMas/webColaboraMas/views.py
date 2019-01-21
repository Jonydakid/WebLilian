from django.shortcuts import render,redirect, reverse
from .forms import FormContacto
from django.core.mail import send_mail
from .models import Mensaje, Curso

# Create your views here.
def index(request):
	return render(request, "index.html", { "titulo": "Index" })

def cursos(request):
	cursos = Curso.objects.all()
	
	return render(request, "cursos.html", { "titulo": "Cursos", "cursos": cursos })

def showCurso(request, idCurso):
	curso=Curso.objects.get(idCurso=idCurso)
	return render(request,"curso.html",{"titulo": curso.nomCurso,"curso":curso})

def contacto(request):
	if request.method == "POST":
		form = FormContacto(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			nombre= data.get("nombre")
			curso = data.get("curso")
			correo=data.get("correo")
			mensaje = data.get("mensaje")
			Mensaje.objects.create(nombre=nombre, curso=curso ,correo=correo, mensaje=mensaje)
			send_mail(
				"Contacto Empresa",
				f"Estimada(o) {nombre} ,Gracias por contactar con nosotras...",
				"donotreplyEmpresa@gmail.com",
				correo,
				fail_silently = True
			)
			return redirect("contacto")
	else:
		form = FormContacto()
    
	return render(request, "contacto.html", { "titulo": "Contactános", "form":form })

def aboutus(request):
	return render(request, "aboutus.html", { "titulo": "Acerca de nosotros" })

def servicioEmpresas(request):
	return render(request, "servicioEmpresas.html", { "titulo": "Servicios a Empresas"})