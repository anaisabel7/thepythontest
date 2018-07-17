from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    pass


class Question(models.Model):
    text = models.CharField(max_length=600, unique=True)
    verified = models.BooleanField(default=False)


class Answer(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    text = models.CharField(max_length=400)
    correct = models.BooleanField(default=False)
