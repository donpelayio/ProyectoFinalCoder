from django.db import models

# Create your models here.
#los diferentes modelos que se crearon dependiendo las clases que se imparten en el gimnasio
class Principiante (models.Model):
    def __str__(self):
        return f"nombre: {self.nombre} - Apellido {self.apellido} - email: {self.email}" 
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

class Intermedio(models.Model):
    def __str__(self):
        return f"nombre: {self.nombre} - Apellido {self.apellido} - email: {self.email} - Peso: {self.peso}" 
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    peso = models.IntegerField()
    
class Avanzado (models.Model):
    def __str__(self):
        return f"nombre: {self.nombre} - Apellido {self.apellido} - email: {self.email} - Peso: {self.peso} - nro Combates: {self.nro_combates}" 
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    peso = models.IntegerField()
    nro_combates = models.IntegerField()
    
class Profesional(models.Model):
    def __str__(self):
        return f"nombre: {self.nombre} - Apellido {self.apellido} - email: {self.email} - Peso: {self.peso} - nro Combates: {self.nro_combates} - edad: {self.edad}" 
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    peso = models.IntegerField()
    nro_combates = models.IntegerField()
    edad = models.IntegerField()
    
    