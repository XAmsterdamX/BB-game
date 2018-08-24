from django.db import models
from game.choices import *

from users.models import CustomUser


class Scenario(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField

    def _str__(self):
        return '%s' % self.name


class Game(models.Model):
    name = models.CharField(max_length=30)
    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    def _str__(self):
        return '%s' % self.name


