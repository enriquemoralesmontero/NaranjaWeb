from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Después de crear cada modelo, hay que hacer un:
# python manage.py makemigrations
# python manage.py migrate

class Categoria(models.Model):

    nombre      = models.CharField(max_length = 50)
    created     = models.DateTimeField(auto_now_add = True)
    updated     = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nombre


class Post(models.Model):

    titulo      = models.CharField(max_length = 50)
    contenido   = models.CharField(max_length = 50)
    imagen      = models.ImageField(upload_to = 'blog', null = True, blank = True)  # Requiere un "pip install Pillow". Las imágenes se guardan en la carpeta "media/blog/"
    autor       = models.ForeignKey(User, on_delete = models.CASCADE)               # Cuando se elimina un usuario, se eliminan sus posts (borrado en cascada).
    categorias  = models.ManyToManyField(Categoria)                                 # Cada post tiene varias categorias y cada categoria tiene varios posts.
    created     = models.DateTimeField(auto_now_add = True)
    updated     = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.titulo

