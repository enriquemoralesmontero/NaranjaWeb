from django.shortcuts import render

# Create your views here.

def tienda(request):
    """ Esta vista busca su plantilla HTML en 'ProyectoNaranja/AppTienda/templates/AppTienda/tienda.html' """
    return render(request, "AppTienda/tienda.html")
