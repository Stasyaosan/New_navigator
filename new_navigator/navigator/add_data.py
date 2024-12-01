from .models import Schedule
from datetime import timedelta, datetime
import json


def get_data_from_json():
    with open('json/data.json') as file:
        data = json.loads(file.read())
        for time, data_list in data['subjects'].items():
            if not Schedule.objects.filter(classroom=data['class'], day_of_week=data['week'], start_time=time).exists():
                schedule = Schedule()
                schedule.classroom = data['class']
                schedule.teacher = data_list[0]
                schedule.lesson = data_list[1]
                schedule.day_of_week = data['week']
                schedule.url = data_list[2]
                schedule.cabinet = data_list[3]
                schedule.day_format = data_list[4]
                schedule.start_time = time
                t = datetime.strptime(time, '%H:%M')
                end_time = t + timedelta(minutes=40)
                end_time = end_time.strftime('%H:%M')
                schedule.end_time = str(end_time)
                schedule.save()
            else:
                s = Schedule.objects.filter(classroom=data['class'], day_of_week=data['week'], start_time=time).first()
                schedule = Schedule(id=s.id)
                schedule.classroom = data['class']
                schedule.teacher = data_list[0]
                schedule.lesson = data_list[1]
                schedule.day_of_week = data['week']
                schedule.url = data_list[2]
                schedule.cabinet = data_list[3]
                schedule.day_format = data_list[4]
                schedule.start_time = time
                t = datetime.strptime(time, '%H:%M')
                end_time = t + timedelta(minutes=40)
                end_time = end_time.strftime('%H:%M')
                schedule.end_time = str(end_time)
                schedule.save()

        return data
