# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..login_app.models import User
from ..play.models import Game
from django.db import models
import re

# Create your models here.
class BoardManager(models.Manager):
    def create_board(self, user_id, game_id):
        new_board = self.create(board = "", game = Game.objects.get(id = game_id), user = User.objects.get(id = user_id))
        return new_board

class Board(models.Model):
    board = models.CharField(max_length =255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    game = models.ForeignKey(Game, related_name="boards")
    user = models.ForeignKey(User, related_name="user_boards")
    objects = BoardManager()
