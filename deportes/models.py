from django.db import models

# Create your models here.
class Deporte(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250,null=True )