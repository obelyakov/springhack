from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
# Create your views here.


def all_result(request):
    team = Team.objects.all().values()
    print(team)

    return JsonResponse({'success': True, 'team':list(team)})

