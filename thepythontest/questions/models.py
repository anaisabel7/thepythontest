from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db import models


class User(AbstractUser):
    score = models.IntegerField(default=0)


class Question(models.Model):
    text = models.CharField(max_length=600, unique=True)
    verified = models.BooleanField(default=False)
    creator = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)


class Answer(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    text = models.CharField(max_length=400)
    correct = models.BooleanField(default=False)
