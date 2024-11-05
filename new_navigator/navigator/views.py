from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.views import View
def index(request):
    return render(request, 'index.html')


class ScheduleListView(View):
    def post(self, request):
        pass
    def get(self, request):
        schedules = Schedule.objects.all()
        events = []
        for schedule in schedules:
            event = {
                'title': schedule.lesson.name + "(" + schedule.teacher.name + ")",
                'start': schedule.day_of_week+"T"+schedule.start_time,
                'end': schedule.day_of_week+"T"+schedule.end_time,
            }
            events.append(event)
        return JsonResponse(events, safe=False)
