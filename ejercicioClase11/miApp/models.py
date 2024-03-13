from django.db import models



class Fabrica(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Sucursale(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Instrumento(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField(max_length=7)
    tipo = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre
