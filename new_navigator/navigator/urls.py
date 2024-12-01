from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('add_schedule', add_schedule)
]
