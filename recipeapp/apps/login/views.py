from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from .forms import UsuarioForm

# Create your views here.

class LoginView(TemplateView):
	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			return redirect('inicio')
		else:
			return render(request, "login.html")

	def post(self, request, *args, **kwargs):
		user = authenticate(username=request.POST.get('email'), password=request.POST.get('password'))
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect('inicio')
		else:
			return render(request, 'login.html', {'mensaje' : 'Usuario y/o password invalido.'})

class RegistroView(TemplateView):
	def get(self, request, *args, **kwargs):
		
		return render(request, "registro.html")

	def post(self, request, *args, **kwargs):
		form = UsuarioForm(request.POST)
		if form.is_valid():

			user = form.save(commit=False)
			user.username = request.POST.get("email")
			user.password = make_password(request.POST.get("password"))
			user.save()

			return redirect("registro")
		else:
			print(form.errors)
			return redirect("inicio")

def LogOut(request):
	logout(request)
	return redirect('login')