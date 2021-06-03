from django.urls import path

from . import views  # = from AppContacto import views

urlpatterns = [
    path('', views.contacto, name="Contacto"),
]
