from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^demo$', views.index, name='demo'),
    url(r'^incoming-message/$', views.incoming, name='incoming'),
]
