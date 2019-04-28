from django.db import models

# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=64)


class Product(models.Model):
    name = models.CharField(max_length=64)
