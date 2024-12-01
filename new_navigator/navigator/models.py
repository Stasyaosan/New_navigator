from django.db import models
class Teacher(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя учителя')
    subject = models.CharField(max_length=100, verbose_name='Предмет')
    url = models.URLField(verbose_name='Ссылка на zoom')

class Classroom(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название класса')

class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название урока')

class Schedule(models.Model):
    classroom = models.CharField(max_length=200)
    teacher = models.CharField(max_length=200)
    lesson = models.CharField(max_length=200)
    day_of_week = models.CharField(max_length=10)
    start_time = models.TimeField()
    end_time = models.TimeField()
    link_zoom = models.URLField()
    cabinet = models.CharField(max_length=50)
    format = models.CharField(max_length=1)