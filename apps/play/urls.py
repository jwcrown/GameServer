# PLAY APP LEVEL
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^new_game$', views.create),
    url(r'^cancel_join/(?P<cancel>\d+)$', views.cancel),
    url(r'^(?P<game_id>\d+)/join$', views.join),
    url(r'^icon$', views.icon),
    url(r'^display/(?P<display_id>\d+)$', views.display),
    url(r'^hide$', views.hide),    
]