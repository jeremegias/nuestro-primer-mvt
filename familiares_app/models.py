from django.db import models


class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()
    def __str__(self):
        return f"{self.id} ,{self.nombre}, {self.direccion}, {self.numero_pasaporte},"

class Automovil(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=200)
    año = models.IntegerField()
    def __str__(self):
        return f"{self.id} ,{self.marca}, {self.modelo}, {self.año},"     

class Mascota(models.Model):
    especie = models.CharField(max_length=100)
    nombre = models.CharField(max_length=200)
    edad = models.IntegerField()
    def __str__(self):
        return f"{self.id} ,{self.especie}, {self.nombre}, {self.edad}," 
