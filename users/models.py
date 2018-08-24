# users/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    organization = models.CharField(max_length=100)
    instructor = models.BooleanField(default=False)

    def __str__(self):
        return self.username
