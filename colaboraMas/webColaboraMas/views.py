from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, "index.html", { "titulo": "Index" })

def cursos(request):
	return render(request, "cursos.html", { "titulo": "Cursos" })

def contacto(request):
	return render(request, "contacto.html", { "titulo": "Contactános" })

def aboutus(request):
	return render(request, "aboutus.html", { "titulo": "Acerca de nosotros" })

def servicioEmpresas(request):
	return render(request, "servicioEmpresas.html", { "titulo": "Servicios a Empresas"})