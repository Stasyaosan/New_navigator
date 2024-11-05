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
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10, choices=[
        ('Monday', 'Понедельник'),
        ('Tuesday', 'Вторник'),
        ('Wednesday', 'Среда'),
        ('Thursday', 'Четверг'),
        ('Friday', 'Пятница'),
    ])
    start_time = models.TimeField()
    end_time = models.TimeField()
