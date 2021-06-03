"""ProyectoNaranja URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include

# Urls del proyecto.
# Incluimos las vistas de la App llamada "AppNaranja", desde el archivo "AppNaranja/urls.py".

urlpatterns = [
    path('admin/', admin.site.urls),                    # localhost:8000/admin/     --> Enlace a al Panel de admin.*
    path('', include('AppNaranja.urls')),               # localhost:8000            --> Enlace a la página principal.
    path('servicios/', include('AppServicios.urls')),   # localhost:8000/servicios  --> Enlace a la página de servicios.
    path('blog/', include('AppBlog.urls')),             # localhost:8000/blog       --> Enlace a la página del blog.
    path('contacto/', include('AppContacto.urls')),     # localhost:8000/contacto   --> Enlace a la página del formul.
]

# *El usuario y contraseña del panel de administración es "root", "1234".