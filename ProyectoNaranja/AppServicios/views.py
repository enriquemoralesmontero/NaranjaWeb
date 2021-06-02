from django.shortcuts import render
from AppServicios.models import Servicio

# Create your views here.

def servicios(request):
    """ Esta vista busca su plantilla HTML en 'ProyectoNaranja/AppServicios/templates/AppServicios/servicios.html' """
    servicios = Servicio.objects.all()  # Importa todos los servicios existentes (todos los objetos de la clase Servicio).
    return render(request, "AppServicios/servicios.html", {"servicios": servicios})
