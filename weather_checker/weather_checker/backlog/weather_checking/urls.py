from django.urls import path

from weather_checker.backlog.weather_checking.views import (index)


app_name = 'weather_checking'

urlpatterns = [
    path('', index, name='index'),
]
