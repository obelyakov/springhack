from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass