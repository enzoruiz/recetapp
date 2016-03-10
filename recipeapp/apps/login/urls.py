from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^logout$', 'apps.login.views.LogOut', name='logout'),
    url(r'^registro/$', RegistroView.as_view(), name="registro"),
]
