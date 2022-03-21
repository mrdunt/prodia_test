from django.urls import path

from weather_checker.backlog.user_loggings.views import (index)


app_name = 'user_loggings'

urlpatterns = [
    path('', index, name='index'),
]
