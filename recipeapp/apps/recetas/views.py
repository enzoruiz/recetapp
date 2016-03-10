from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core import serializers
from django.http import HttpResponse
from .models import *

# Create your views here.

class InicioView(TemplateView):
	def get(self, request, *args, **kwargs):
		recetas = Receta.objects.all().extra(select={'resultado': "puntuacion_positiva - puntuacion_negativa"}).order_by('-resultado')
		for rec in recetas:
			rec.resultado = rec.puntuacion_positiva - rec.puntuacion_negativa

		return render(request, "inicio.html", { "recetas" : recetas })

	def post(self, request, *args, **kwargs):
		if request.is_ajax():
			if request.POST.get('opcion') == 'calificar':
				if request.POST.get('tipo') == 'positivo':
					receta = Receta.objects.get(id=request.POST.get('id_receta'))
					receta.puntuacion_positiva = receta.puntuacion_positiva + 1
					receta.save()
				else:
					receta = Receta.objects.get(id=request.POST.get('id_receta'))
					receta.puntuacion_negativa = receta.puntuacion_negativa + 1
					receta.save()
				
				recetas = Receta.objects.all().extra(select={'resultado': "puntuacion_positiva - puntuacion_negativa"}).order_by('-resultado')
				data = serializers.serialize('json', recetas)
				return HttpResponse(data, content_type="application/json")
		else:
			receta = Receta()
			receta.descripcion = request.POST.get("descripcion")
			receta.usuario = User.objects.get(id=request.POST.get("usuario"))
			receta.save()

			return redirect("inicio")