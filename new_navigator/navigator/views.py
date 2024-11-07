from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.views import View


def index(request):
    return render(request, 'index.html')


class ScheduleListView(View):
    def get(self, request):
        schedules = Schedule.objects.all()
        events = []

        #schedule.day_of_week+"T"
        for schedule in schedules:
            print(str(schedule.start_time)[:5])
            day = 0
            if schedule.day_of_week == 'Monday':
                day = 1
            elif schedule.day_of_week == 'Tuesday':
                day = 2
            elif schedule.day_of_week == 'Wednesday':
                day = 3
            elif schedule.day_of_week == 'Thursday':
                day = 4
            elif schedule.day_of_week == 'Friday':
                day = 5
            event = {
                'title': schedule.lesson.name + "(" + schedule.teacher.name + ")",
                'daysOfWeek': f'[{day}]',
                'startTime': str(schedule.start_time)[:5],
                'endTime': str(schedule.end_time)[:5],
                'backgroundColor': '#000'
            }
            events.append(event)
        return JsonResponse(events, safe=False)
