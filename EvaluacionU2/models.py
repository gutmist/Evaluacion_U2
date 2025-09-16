from django.db import models

# Create your models here.
class Pelicula(models.Model):
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    director = models.CharField(max_length=100)
    año = models.IntegerField()

    def __str__(self):
        return self.nombre