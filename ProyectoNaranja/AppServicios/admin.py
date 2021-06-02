from django.contrib import admin
from .models import Servicio

# Register your models here.

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated') # En el panel de administración, estos dos campos de Servicio aparecerán de sólo lectura.

admin.site.register(Servicio, ServicioAdmin) # Ahora aparecerán los servicios en el panel de administración.