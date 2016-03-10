from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Receta(models.Model):
	descripcion = models.CharField(max_length=400)
	puntuacion_positiva = models.IntegerField(default=0)
	puntuacion_negativa = models.IntegerField(default=0)
	fecha_creacion = models.DateField(auto_now=True)
	usuario = models.ForeignKey(User)