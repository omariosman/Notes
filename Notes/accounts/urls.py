from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView

app_name = 'accounts'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', LoginView.as_view(), {'template_name' : 'login.html'})
]
