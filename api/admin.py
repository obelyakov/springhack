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