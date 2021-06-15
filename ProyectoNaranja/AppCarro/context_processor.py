
# Almacén de variables globales.
# Hay que registrarlo en "settings.py" en "context_processors".

def importe_total_carro(request):

    total = 0

    if request.user.is_authenticated or True:  # Quitar el "or True" cuando se implemente la autenticación de usuario.
        for key, value in request.session["carro"].items():
            total += float(value["precio"])

    return {"importe_total_carro": total}
