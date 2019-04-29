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



class ProgrammerRating(models.Model):
    code_awerage = models.IntegerField("Покрытие тестами")
    ended_task = models.IntegerField("Закрытых задач")
    returned_task = models.IntegerField("Возвращенных задач от QA")
    pep8 = models.IntegerField("Следование стандартам кода")
    stendap = models.IntegerField("Участие в стендапах")
    awerage_team_rate = models.IntegerField("Уcредненная оценка коллегами")
    date = models.DateField('Дата оценки')
    member = models.ForeignKey(to=Programmer, verbose_name="Участник", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Рейтинг программиста"

    def __str__(self):
        return "Рейтинги программиста"










