from django.shortcuts import render
from .models import Schedule
from django.http import JsonResponse
from django.views import View
from .add_data import get_data_from_json


def index(request):
    schedules = Schedule.objects.filter(day_of_week='Monday')
    return render(request, 'index_.html', context={'schedules': schedules})


def add_schedule(request):
    get_data_from_json()
