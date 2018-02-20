# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import bcrypt
import re

# Create your models here.


class UserManager(models.Manager):
    def validate(self, postData):
        results = {'status': True, 'errors': []}
        if len(postData['name']) < 3:
            results['errors'].append('Your name is too short.')
            results['status'] = False
        if not re.match("^[a-zA-Z ]*$", postData['name']):
            results['errors'].append('Name cannot contain numbers or special characters')
            results['status'] = False
        if len(postData['username']) < 3:
            results['errors'].append('Your username is too short.')
            results['status'] = False
        if len(postData['password']) < 8:
            results['errors'].append('Password is too short')
            results['status'] = False
        if postData['password'] != postData['c_password']:
            results['errors'].append('Passwords do not match')
            results['status'] = False
        if len(self.filter(username = postData['username'])) > 0:
            results['errors'].append('Username entered is already registered.')
            results['status'] = False
        return results

    def creator(self, postData):
        user = self.create(name = postData['name'], username = postData['username'], password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()), wins = 0, loses = 0, rank = 0, icon = postData['icon'])
        return user

    def loginVal(self, postData):
        results = {'status': True, 'errors': [], 'user': None}
        users = self.filter(username = postData['username'])
        if len(users) < 1:
            results['status'] = False
        else:
            if bcrypt.checkpw(postData['password'].encode(), users[0].password.encode()):
                results['user'] = users[0]
            else:
                results['status'] = False
        return results
    
    def rank(self, user_id):
        rank_sum = User.objects.get(id = user_id)
        rank_sum.rank = rank_sum.wins - rank_sum.loses
        rank_sum.save()
        return rank_sum
            
class User(models.Model):
    name = models.CharField(max_length =255)
    username = models.CharField(max_length =255)
    password = models.CharField(max_length =255)
    icon = models.CharField(max_length =255)
    rank = models.IntegerField()
    wins = models.IntegerField()
    loses = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    objects = UserManager()