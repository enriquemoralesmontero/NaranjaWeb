from django.urls import path
from django.conf import settings            # Para ver las imágenes de la carpeta "/media".
from django.conf.urls.static import static  # Para ver las imágenes de la carpeta "/media".
from AppServicios import views

urlpatterns = [
    path('', views.servicios, name="Servicios"),
]

# Para ver las imágenes de la carpeta "/media".
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)