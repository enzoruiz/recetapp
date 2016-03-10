from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    url(r'^$', login_required(InicioView.as_view()), name="inicio"),
]
