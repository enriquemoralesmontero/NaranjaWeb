from django.urls import path
from . import views

# Urls de la app llamada "AppNaranja". Será incluida en "urls.py" de "ProyectoNaranja".

urlpatterns = [
    path('', views.tienda, name="Tienda"),
]
