from django.urls import path

from weather_checker.backlog.areas.views import (index)


app_name = 'areas'

urlpatterns = [
    path('', index, name='index'),
]
