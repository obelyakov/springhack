from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductOwner)
class ProductOwnerAdmin(admin.ModelAdmin):
    pass


@admin.register(TeamLid)
class TeamLidAdmin(admin.ModelAdmin):
    pass


@admin.register(Programmer)
class ProgrammerAdmin(admin.ModelAdmin):
    pass


@admin.register(Analit)
class AnalitAdmin(admin.ModelAdmin):
    pass


@admin.register(Tester)
class TesterAdmin(admin.ModelAdmin):
    pass


@admin.register(Devops)
class DevopsAdmin(admin.ModelAdmin):
    pass


@admin.register(Administrator)
class AdministratorAdmin(admin.ModelAdmin):
    pass

@admin.register(ProgrammerRating)
class ProgrammerRatingAdmin(admin.ModelAdmin):
    list_display = ( 'date', 'member', 'code_awerage', 'ended_task', 'returned_task', 'pep8', 'stendap', 'awerage_team_rate')

"""
    code_awerage = models.IntegerField("Покрытие тестами")
    ended_task = models.IntegerField("Закрытых задач")
    returned_task = models.IntegerField("Возвращенных задач от QA")
    pep8 = models.IntegerField("Следование стандартам кода")
    stendap = models.IntegerField("Участие в стендапах")
    awerage_team_rate = models.IntegerField("Уcредненная оценка коллегами")
    date = models.DateField('Дата оценки')
    member = models.ForeignKey(to=Programmer, verbose_name="Участник", on_delete=models.CASCADE)

"""