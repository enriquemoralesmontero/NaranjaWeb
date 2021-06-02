from django.db import models

# Create your models here.

# Después de crear cada modelo, hay que hacer un:
# python manage.py makemigrations
# python manage.py migrate

class Servicio(models.Model):
    titulo      = models.CharField(max_length = 50)
    contenido   = models.CharField(max_length = 50)
    imagen      = models.ImageField(upload_to = 'servicios')    # Requiere un "pip install Pillow". Las imágenes se guardan en la carpeta "media/servicios/"
    #imagen = models.ImageField()  # Requiere un "pip install Pillow". Las imágenes se guardan en la carpeta "media/servicios/"
    created     = models.DateTimeField(auto_now_add = True)
    updated     = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'

    def __str__(self):
        return self.titulo

