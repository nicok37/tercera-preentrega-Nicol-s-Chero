from django.db import models
# Create your models here.

class Estudiantes(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    email = models.EmailField()

    def _str__(self):
        return f"{self.nombre} - {self.apellido}"#en base de datos se muestra así admin de django

class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField()
    def _str__(self):
        return f"{self.nombre} - {self.comision}"#en base de datos se muestra así admin de django


class Entregable(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_entrega = models.DateTimeField()
    descripcion = models.TextField()
    def _str__(self):
        return f"{self.nombre} - {self.fecha_entrega} - "#en base de datos se muestra así de admin django

    
class Profesor(models.Model):  
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    email = models.EmailField() 
    def _str__(self):
        return f"{self.nombre} - {self.apellido}"#en base de datos se muestra así
