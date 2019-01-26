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
			mensaje = data.get("mensaje")
			cor=[data.get("correo"),"jonathan.torres.salvo@gmail.com"]
			Mensaje.objects.create(nombre=nombre, curso=curso ,correo=data.get("correo"), mensaje=mensaje)
			send_mail(
				"Contacto Talento y Belleza",
				f"Estimada(o) {nombre} ,Gracias por contactar con nosotras\n Acaba de realizar una consulta acerca de"+
				f"nuestro curso de {curso}\n cuyo mensaje fue '{mensaje}'",
				"donotreplytalentoybelleza@gmail.com",
				cor,
				fail_silently = True
			)
			return redirect("contacto")
	else:
		form = FormContacto()
    
	return render(request, "contacto.html", { "titulo": "Contactános", "form":form })

def aboutus(request):
	return render(request, "aboutus.html", { "titulo": "Acerca de nosotros" })

def servicioEmpresas(request):
	
	return render(request, "servicioEmpresas.html", { "titulo": "Servicio a empresas"})

def promociones(request):
    return render(request, "promociones.html", { "titulo": "Promociones" })