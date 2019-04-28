from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
# Create your views here.


def all_result(request):
    team = list(Team.objects.all().values())
    product = list(Product.objects.all().values())
    product_owner = list(ProductOwner.objects.all().values())
    team_lid = list(TeamLid.objects.all().values())
    programmer = list(Programmer.objects.all().values())
    analit = list(Analit.objects.all().values())
    tester = list(Tester.objects.all().values())
    devops = list(Devops.objects.all().values())
    administrator = list(Administrator.objects.all().values())
    

    return JsonResponse(
        {
        'success': True, 
        'team':team,
        'product': product,
        'product_owner': product_owner,
        'team_lid': team_lid,
        'programmer': programmer,
        'analit': analit,
        'tester': tester,
        'devops': devops,
        'administrator': administrator,
        'member': {'name': 'Иванов Иван Иваныч',
                    'position': 'Старший программист',
                    'current_gazcoin': 125,
                    'future_gazcoin': 12,
                    'rating': 1723,
                    'relatively_rating_persing': 25,
                    'achievement_list': [
                                            'Прошел курсы личного развития',
                                            'Программист года',
                                            'Прочитал лекцию',
                                            'Любимчик команды',
                                            'Начальство одобряет',
                                            'Всю неделю исправно ходил на стендапы',
                                            'Лучшее покрытие кода тестами'
                                            ]
                    },
        '360view': {
                    'me': {'Креативный':50, "Отзывчивый":70, "Вовлеченный":90, "Позитивный":50, "Вдохновляющий": 90, "Трудолюбивый":40, "Инновационный":95}, 
                    'other': {'Креативный':40, "Отзывчивый":75, "Вовлеченный":95, "Позитивный":40, "Вдохновляющий": 100, "Трудолюбивый":70, "Инновационный":100}
                    },
        'personal_index': {
                            'close_task_persent':90,
                            'rollback_persent': 100,
                            'work_speed':70,
                            'chat_answer_speed':80,
                            'awerage_team_rating': 85,
                            'match_assessment': 100

                        },
        'product_index': {
                            'user_count': 43546,
                            'app_rating': 4.5,
                            'csi': 85,
                            'arpu': 19
                            },
        'weekly_quest': {
                        'text': 'Полить цветы',
                        'steps': [1,1,1,0]
                        },
        'top3_user_comment': [
                                '..после установки приложения выровнялось давление, прошли головные боли...',
                                '..посоветовал друг, что могу скать, все клево. Все работает',
                                'Отличное приложение, ждем того же приложения для Nokia 3310',
                                ]




        }
)

        

