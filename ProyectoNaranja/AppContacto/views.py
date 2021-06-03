from django.shortcuts import render

# Create your views here.

def contacto(request):
    """ Esta vista busca su plantilla HTML en 'ProyectoNaranja/AppNaranja/templates/AppNaranja/contacto.html' """
    return render(request, "AppContacto/contacto.html")