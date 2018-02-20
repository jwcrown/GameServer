# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from ..login_app.models import User
from ..battleship_app.models import Board
from models import Game
from django.contrib import messages
# Create your views here.

def index(request):
    if 'username' not in request.session:
        return redirect('/')

    rank_cal = User.objects.rank(request.session['id'])
    if 'display' not in request.session:
        game_list = {
            "my_games": User.objects.get(id = request.session['id']).games.all(),
            "join_games": Game.objects.exclude(players = User.objects.get(id = request.session['id'])),
            "rank": User.objects.all().order_by('-rank'),
            "user": User.objects.get(id = request.session['id']),
        }
        return render(request, 'play/index.html', game_list)
    else:
        game_list = {
            "my_games": User.objects.get(id = request.session['id']).games.all(),
            "join_games": Game.objects.exclude(players = User.objects.get(id = request.session['id'])),
            "rank": User.objects.all().order_by('-rank'),
            "user": User.objects.get(id = request.session['id']),
            "display": User.objects.get(id = request.session['display'])
        }
        return render(request, 'play/index.html', game_list)

def create(request):
    new_game = Game.objects.create_game(request.POST, request.session['id'])
    game_id = new_game.id
    new_board = Board.objects.create_board(request.session['id'], game_id)
    return redirect('/play')

def cancel(request, cancel):
    Game.objects.get(id = cancel).delete()
    return redirect('/play')

def join(request, game_id):
    player = User.objects.get(id = request.session['id'])
    player.games.add(game_id)
    player.save()
    new_board = Board.objects.create_board(request.session['id'], game_id)
    return redirect('/play')

def icon(request):
    icon_update = User.objects.get(id = request.session['id'])
    print icon_update
    print request.POST['icon']
    icon_update.icon = request.POST['icon']
    icon_update.save()
    return redirect('/play')

def display(request, display_id):
    if 'display' not in request.session:
        request.session['display'] = display_id
    else:
        del request.session['display']
        request.session['display'] = display_id
    return redirect('/play')


def hide(request):
    del request.session['display']
    return redirect('/play')
    