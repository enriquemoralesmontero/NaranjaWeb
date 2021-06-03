from django.shortcuts import render
from AppBlog.models import Post, Categoria

# Create your views here.

def blog(request):
    """ Esta vista busca su plantilla HTML en 'ProyectoNaranja/AppBlog/templates/AppBlog/blog.html' """
    posts = Post.objects.all()  # Importa todos los posts existentes (todos los objetos de la clase Post).
    return render(request, "AppBlog/blog.html", {"posts": posts})

def categoria(request, categoria_id):  # Le pasamos el id de categoria por parámetro para filtrar. Ver urls.py
    categoria = Categoria.objects.get(id=categoria_id)
    posts = Post.objects.filter(categorias = categoria)
    return render(request, "AppBlog/categoria.html", {"categoria": categoria, "posts": posts})
