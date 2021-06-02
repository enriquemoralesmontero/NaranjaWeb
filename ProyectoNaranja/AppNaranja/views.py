from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    """ Esta vista busca su plantilla HTML en 'ProyectoNaranja/AppNaranja/templates/AppNaranja/blog.html' """
    return render(request, "AppNaranja/home.html")

def tienda(request):
    """ Esta vista busca su plantilla HTML en 'ProyectoNaranja/AppNaranja/templates/AppNaranja/tienda.html' """
    return render(request, "AppNaranja/tienda.html")

def contacto(request):
    """ Esta vista busca su plantilla HTML en 'ProyectoNaranja/AppNaranja/templates/AppNaranja/contacto.html' """
    return render(request, "AppNaranja/contacto.html")
