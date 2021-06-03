from django.shortcuts import render
from .forms import FormularioContacto

# Create your views here.

def contacto(request):
    """ Esta vista busca su plantilla HTML en 'ProyectoNaranja/AppContacto/templates/AppContacto/contacto.html' """
    formulario_contacto = FormularioContacto()
    return render(request, "AppContacto/contacto.html", {'miformulario':formulario_contacto})