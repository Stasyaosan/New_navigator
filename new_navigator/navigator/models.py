from django.db import models


class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название урока')

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя учителя')
    url = models.URLField(verbose_name='Ссылка на zoom')
    lesson = models.ManyToManyField(Lesson)

    def __str__(self):
        return self.name


class Classroom(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название класса')

    def __str__(self):
        return self.name


class Schedule(models.Model):
    classroom = models.CharField(max_length=10)
    teacher = models.CharField(max_length=50)
    lesson = models.CharField(max_length=50)
    day_of_week = models.CharField(max_length=10)
    start_time = models.TimeField()
    end_time = models.TimeField()
    url = models.URLField()
    cabinet = models.CharField(max_length=10)
    day_format = models.CharField(max_length=1)

    def __str__(self):
        return self.day_of_week
