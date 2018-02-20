# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from ..login_app.models import User
from ..play.models import Game
from models import Board
from django.contrib import messages
# Create your views here.

def index(request, game_id):
    game_list = {
        "user": User.objects.get(id = request.session['id']),
        "game": Game.objects.get(id = game_id),
        "board": Board.objects.filter(game = game_id),
    }
    return render(request, 'battleship_app/index.html', game_list)
