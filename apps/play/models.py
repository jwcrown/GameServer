# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..login_app.models import User
from django.db import models
import re

# Create your models here.
class GameManager(models.Manager):
    def create_game(self, postData, user_id):
        new_game = self.create(game_type = postData['game_type'], game_desc = postData['game_desc'], turn = 0)
        player = User.objects.get(id = user_id)
        player.games.add(new_game)
        player.save()
        return new_game

class Game(models.Model):
    game_type = models.CharField(max_length =255)
    game_desc = models.CharField(max_length =255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    players = models.ManyToManyField(User, related_name="games")
    turn = models.IntegerField()
    objects = GameManager()


