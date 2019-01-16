from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
	url(r"^aboutus/$", views.aboutus, name = "aboutus"),
	url(r"^cursos/$", views.cursos, name = "cursos"),
	url(r"^contacto/$", views.contacto, name = "contacto"),
	url(r"^$", views.index, name = "index"),
]