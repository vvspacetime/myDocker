from django.conf.urls import url

from . import views

app_name = 'hellodocker'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/(?P<app_id>[0-9]*)',views.api, name="api"),
]