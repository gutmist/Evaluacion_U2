from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Pelicula
from .forms import PeliculaForm

def listar_peliculas(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'lista_peliculas.html', {'peliculas': peliculas})

def crear_pelicula(request):
    if request.method == 'POST':
        form = PeliculaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_peliculas')
    else:
        form = PeliculaForm()
    return render(request, 'crear_pelicula.html', {'form': form})
