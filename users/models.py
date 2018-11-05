from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
	age = models.PositiveIntegerField(null=True, blank=True)


class Game(models.Model):
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	score = models.PositiveIntegerField(null=True, blank=True)