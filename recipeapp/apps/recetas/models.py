from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Receta(models.Model):
	titulo = models.CharField(max_length=45)
	descripcion = models.CharField(max_length=500)
	puntuacion_positiva = models.IntegerField(default=0)
	puntuacion_negativa = models.IntegerField(default=0)
	fecha_creacion = models.DateField(auto_now=True)
	imagen = models.ImageField(upload_to="img-receta", blank=True, null=True)
	usuario = models.ForeignKey(User)

class PuntuacionRecetaUser(models.Model):
	puntuacion = models.CharField(max_length=1)
	receta = models.ForeignKey(Receta)
	usuario = models.ForeignKey(User)