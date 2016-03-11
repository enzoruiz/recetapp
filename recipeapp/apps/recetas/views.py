from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core import serializers
from django.http import HttpResponse
from .models import *
import json

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
				pru = PuntuacionRecetaUser.objects.filter(usuario=User.objects.get(id=request.POST.get("usuario")), receta=Receta.objects.get(id=request.POST.get("id_receta")))
				
				if request.POST.get('tipo') == 'positivo':
					if len(pru) > 0:
						# CADA USUARIO SOLO PUEDE CALIFICAR UNA VES POR RECETA
						# PUEDE CAMBIAR SU CALIFICACION DE POSITIVA A NEGATIVA O VICEVERSA
						if pru[0].puntuacion == 'N':
							receta = Receta.objects.get(id=request.POST.get('id_receta'))
							receta.puntuacion_positiva = receta.puntuacion_positiva + 1
							receta.puntuacion_negativa = receta.puntuacion_negativa - 1
							receta.save()

							PuntuacionRecetaUser.objects.get(usuario=User.objects.get(id=request.POST.get("usuario")), receta=Receta.objects.get(id=request.POST.get("id_receta"))).delete()

							p = PuntuacionRecetaUser()
							p.puntuacion = 'P'
							p.receta = receta
							p.usuario = User.objects.get(id=receta.usuario.id)
							p.save()
					else:
						receta = Receta.objects.get(id=request.POST.get('id_receta'))
						receta.puntuacion_positiva = receta.puntuacion_positiva + 1
						receta.save()

						p = PuntuacionRecetaUser()
						p.puntuacion = 'P'
						p.receta = receta
						p.usuario = User.objects.get(id=receta.usuario.id)
						p.save()

				else:
					if len(pru) > 0:
						# CADA USUARIO SOLO PUEDE CALIFICAR UNA VES POR RECETA
						# PUEDE CAMBIAR SU CALIFICACION DE POSITIVA A NEGATIVA O VICEVERSA
						if pru[0].puntuacion == 'P':
							receta = Receta.objects.get(id=request.POST.get('id_receta'))
							receta.puntuacion_positiva = receta.puntuacion_positiva - 1
							receta.puntuacion_negativa = receta.puntuacion_negativa + 1
							receta.save()

							PuntuacionRecetaUser.objects.get(usuario=User.objects.get(id=request.POST.get("usuario")), receta=Receta.objects.get(id=request.POST.get("id_receta"))).delete()

							p = PuntuacionRecetaUser()
							p.puntuacion = 'N'
							p.receta = receta
							p.usuario = User.objects.get(id=receta.usuario.id)
							p.save()
					else:
						receta = Receta.objects.get(id=request.POST.get('id_receta'))
						receta.puntuacion_negativa = receta.puntuacion_negativa + 1
						receta.save()

						p = PuntuacionRecetaUser()
						p.puntuacion = 'N'
						p.receta = receta
						p.usuario = User.objects.get(id=receta.usuario.id)
						p.save()

				recetas = Receta.objects.all().extra(select={'resultado': 'puntuacion_positiva - puntuacion_negativa'}).values('id', 'titulo', 'descripcion', 'usuario__first_name', 'usuario__last_name', 'puntuacion_positiva', 'puntuacion_negativa', 'resultado', 'fecha_creacion', 'imagen').order_by('-resultado')
				for re in recetas:
					re["fecha_creacion"] = re["fecha_creacion"].strftime("%d/%m/%Y")

				data = json.dumps(list(recetas))
				return HttpResponse(data, content_type="application/json")
		else:
			receta = Receta()
			receta.titulo = request.POST.get("titulo")
			try:
				receta.imagen = request.FILES['imagen']
			except Exception:
				print("NO SUBIO IMAGEN PARA RECETA")
				pass
			
			receta.descripcion = request.POST.get("descripcion")
			receta.usuario = User.objects.get(id=request.POST.get("usuario"))
			receta.save()

			return redirect("inicio")