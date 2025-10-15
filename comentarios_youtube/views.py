from django.shortcuts import render, redirect, get_object_or_404
from .models import ComentarioYouTube
from .forms import ComentarioYouTubeForm

def lista_comentarios(request):
    comentarios = ComentarioYouTube.objects.all()
    return render(request, 'comentarios_youtube/lista_comentarios.html', {'comentarios': comentarios})

def agregar_comentario(request):
    if request.method == 'POST':
        form = ComentarioYouTubeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_comentarios')
    else:
        form = ComentarioYouTubeForm()
    return render(request, 'comentarios_youtube/agregar_comentario.html', {'form': form})

def editar_comentario(request, pk):
    comentario = get_object_or_404(ComentarioYouTube, pk=pk)
    if request.method == 'POST':
        form = ComentarioYouTubeForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            return redirect('lista_comentarios')
    else:
        form = ComentarioYouTubeForm(instance=comentario)
    return render(request, 'comentarios_youtube/editar_comentario.html', {'form': form})

def eliminar_comentario(request, pk):
    comentario = get_object_or_404(ComentarioYouTube, pk=pk)
    if request.method == 'POST':
        comentario.delete()
        return redirect('lista_comentarios')
    return render(request, 'comentarios_youtube/confirmar_eliminar.html', {'comentario': comentario})