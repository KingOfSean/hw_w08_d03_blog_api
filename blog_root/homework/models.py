from django.db import models

class Homework(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=100)
