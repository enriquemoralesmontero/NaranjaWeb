from django.shortcuts import render
from .models import Producto

# Create your views here.

def tienda(request):
    """ Esta vista busca su plantilla HTML en 'ProyectoNaranja/AppTienda/templates/AppTienda/tienda.html' """
    productos = Producto.objects.all()
    return render(request, "AppTienda/tienda.html", {"productos": productos})
