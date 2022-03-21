from django.urls import path

from weather_checker.backlog.areas.views import (index, create_area, update_area)


app_name = 'areas'

urlpatterns = [
    path('', index, name='index'),
    path('create/', create_area, name='create_area'),
    path('update/<str:id>', update_area, name="update_area"),
]
