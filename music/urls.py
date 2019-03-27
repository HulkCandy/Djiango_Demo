#_*_Coding:utf-8_*_
from django.conf.urls import url
from . import views

urlpatterns = [
    #/music/
    url(r'^$',views.index,name='index'),
    #/music/712/
    #^ =begining $=ending
    url(r'^(?P<album_id>[0-9]+)$', views.detail, name=''),
]

