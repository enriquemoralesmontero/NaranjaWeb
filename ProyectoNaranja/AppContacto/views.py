from django.shortcuts import render, redirect
from .forms import FormularioContacto

# Create your views here.

def contacto(request):
    """ Esta vista busca su plantilla HTML en 'ProyectoNaranja/AppContacto/templates/AppContacto/contacto.html' """
    formulario_contacto = FormularioContacto()  # Si ha entrado en la web sin darle al submit.
    if request.method == "POST":                # Si le ha dado al botón submit.
        formulario_contacto = FormularioContacto(data = request.POST)
        if formulario_contacto.is_valid():
            nombre    = request.POST.get("nombre")  # ¡¡Datos del formulario pasados a una variable!!
            email     = request.POST.get("email")
            contenido = request.POST.get("contenido")
            return redirect("/contacto/?ok")
    return render(request, "AppContacto/contacto.html", {'miformulario':formulario_contacto})