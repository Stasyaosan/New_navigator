from .models import Schedule
import json
from datetime import datetime, timedelta
def get_data_from_json():
    with open('json/data.json') as f:
        data = json.loads(f.read())
        for time, data_list in data['subjects'].items():

            t = datetime.strptime(time, '%H:%M')
            end_time = t + timedelta(minutes=40)
            end_time = end_time.strftime('%H:%M')
            if not Schedule.objects.filter(classroom=data['class'], day_of_week=data['week'], start_time=time).exists():
                schedule = Schedule()
                schedule.classroom = data['class']
                schedule.teacher = data_list[0]
                schedule.lesson = data_list[1]
                schedule.day_of_week = data['week']
                schedule.start_time = time
                schedule.end_time = str(end_time)
                schedule.link_zoom = data_list[2]
                schedule.cabinet = data_list[3]
                schedule.format = data_list[4]
                schedule.save()
            else:
                s = Schedule.objects.filter(classroom=data['class'], day_of_week=data['week'], start_time=time).first()
                schedule = Schedule(id=s.id)
                schedule.classroom = data['class']
                schedule.teacher = data_list[0]
                schedule.lesson = data_list[1]
                schedule.day_of_week = data['week']
                schedule.start_time = time
                schedule.end_time = str(end_time)
                schedule.link_zoom = data_list[2]
                schedule.cabinet = data_list[3]
                schedule.format = data_list[4]
                schedule.save()
        
