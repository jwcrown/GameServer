# Battleship APP LEVEL
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^(?P<game_id>\d+)$', views.index),
]