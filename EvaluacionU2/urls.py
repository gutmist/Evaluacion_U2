from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_peliculas, name='listar_peliculas'),
    path('crear/', views.crear_pelicula, name='crear_pelicula'),
]
