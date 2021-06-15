from django.urls import path
from . import views

# Urls de la app llamada "AppNaranja". Será incluida en "urls.py" de "ProyectoNaranja".

# Namespace para facilitarnos la vida.
app_name = "carro"

urlpatterns = [
    path("agregar/<int:producto_id>/", views.agregar_producto, name="agregar"),
    path("eliminar/<int:producto_id>/", views.eliminar_producto, name="eliminar"),
    path("restar/<int:producto_id>/", views.restar_producto, name="restar"),
    path("limpiar/", views.limpiar_carro, name="limpiar"),
]
