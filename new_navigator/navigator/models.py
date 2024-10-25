from django.db import models


class Lesson(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    cabinet = models.CharField(max_length=10)


class SchoolDay(models.Model):
    title = models.CharField(max_length=100)
    format = models.CharField(max_length=100)

