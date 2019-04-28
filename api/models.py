from django.db import models

# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class ProductOwner(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class TeamLid(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Programmer(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Analit(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Tester(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Devops(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Administrator(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


















    