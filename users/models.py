from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=150)
    username = models.CharField(max_length=150)
    age = models.IntegerField()
    points = models.IntegerField()
