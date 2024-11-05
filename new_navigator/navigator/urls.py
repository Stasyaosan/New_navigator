from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('api/schedule/', ScheduleListView.as_view(), name='schedule-list')
]
