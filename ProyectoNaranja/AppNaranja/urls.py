from django.urls import path
from django.conf import settings            # Para ver las imágenes de la carpeta "/media".
from django.conf.urls.static import static  # Para ver las imágenes de la carpeta "/media".
from AppNaranja import views

# Urls de la app llamada "AppNaranja". Será incluida en "urls.py" de "ProyectoNaranja".

urlpatterns = [
    path('', views.home, name="Home"),
    path('tienda', views.tienda, name="Tienda"),
    path('contacto', views.contacto, name="Contacto"),
]


# Para ver las imágenes de la carpeta "/media".

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)