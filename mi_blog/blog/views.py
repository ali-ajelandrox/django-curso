from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Publicacion, Comentario
from .forms import PublicacionForm, ComentarioForm

def lista_publicaciones(request):
    publicaciones = Publicacion.objects.all()
    return render(request, 'blog/lista_publicaciones.html', {'publicaciones': publicaciones})

def detalle_publicacion(request, id):
    publicacion = get_object_or_404(Publicacion, id=id)
    comentarios = publicacion.comentarios.all()
    form = ComentarioForm()
    return render(request, 'blog/detalle_publicacion.html', {'publicacion': publicacion, 'comentarios': comentarios, 'form': form})

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('iniciar_sesion')
    else:
        form = UserCreationForm()
    return render(request, 'blog/registro.html', {'form': form})

def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('lista_publicaciones')
    return render(request, 'blog/iniciar_sesion.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('lista_publicaciones')

def crear_publicacion(request):
    if request.method == 'POST':
        form = PublicacionForm(request.POST, request.FILES)
        if form.is_valid():
            publicacion = form.save(commit=False)
            publicacion.autor = request.user
            publicacion.save()
            return redirect('lista_publicaciones')  # Redirige a la lista de publicaciones
    else:
        form = PublicacionForm()
    return render(request, 'blog/crear_publicacion.html', {'form': form})


def agregar_comentario(request, id):
    publicacion = get_object_or_404(Publicacion, id=id)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.publicacion = publicacion
            comentario.autor = request.user
            comentario.save()
            return redirect('detalle_publicacion', id=publicacion.id)
    return redirect('detalle_publicacion', id=publicacion.id)


# Create your views here.
