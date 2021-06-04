from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage

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
            email = EmailMessage("Mensaje naranja",
                                 "Usuario: {}\nCorreo: {}\n\nContenido:\n\n{}".format(nombre, email, contenido),
                                 "",
                                 ["xxxxxxxxxxxxxxxxxxxxxx@gmail.com"],
                                 reply_to=[email])
            try:
                email.send()
                return redirect("/contacto/?ok")
            except:
                return redirect("/contacto/?error")
    return render(request, "AppContacto/contacto.html", {'miformulario':formulario_contacto})