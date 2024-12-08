# from .models import Schedule
from datetime import timedelta, datetime
import json


def add_data_from_json():
    with open('json/data.json') as file:
        data = json.loads(file.read())
        print(data)
        for day in data:
            for time, day_list in day['subjects'].items():
                if not Schedule.objects.filter(classroom=day['class'], day_of_week=day['week'],
                                               start_time=time).exists():
                    schedule = Schedule()
                    schedule.classroom = day['class']
                    schedule.teacher = day_list[0]
                    schedule.lesson = day_list[1]
                    schedule.day_of_week = day['week']
                    schedule.url = day_list[2]
                    schedule.cabinet = day_list[3]
                    schedule.day_format = day_list[4]
                    schedule.start_time = time
                    t = datetime.strptime(time, '%H:%M')
                    end_time = t + timedelta(minutes=40)
                    end_time = end_time.strftime('%H:%M')
                    schedule.end_time = str(end_time)
                    schedule.save()
                else:
                    s = Schedule.objects.filter(classroom=day['class'], day_of_week=day['week'],
                                                start_time=time).first()
                    schedule = Schedule(id=s.id)
                    schedule.classroom = day['class']
                    schedule.teacher = day_list[0]
                    schedule.lesson = day_list[1]
                    schedule.day_of_week = day['week']
                    schedule.url = day_list[2]
                    schedule.cabinet = day_list[3]
                    schedule.day_format = day_list[4]
                    schedule.start_time = time
                    t = datetime.strptime(time, '%H:%M')
                    end_time = t + timedelta(minutes=40)
                    end_time = end_time.strftime('%H:%M')
                    schedule.end_time = str(end_time)
                    schedule.save()
