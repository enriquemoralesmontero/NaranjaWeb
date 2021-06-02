from django.shortcuts import render
from AppBlog.models import Post

# Create your views here.

def blog(request):
    """ Esta vista busca su plantilla HTML en 'ProyectoNaranja/AppBlog/templates/AppBlog/blog.html' """
    posts = Post.objects.all()  # Importa todos los posts existentes (todos los objetos de la clase Post).
    return render(request, "AppBlog/blog.html", {"posts": posts})
