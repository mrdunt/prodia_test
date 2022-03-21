from django.urls import path, include

app_name = 'backlog'

urlpatterns = [
    path('areas/', include(
        'weather_checker.backlog.areas.urls', namespace='areas')),

    path('weather_checking/', include(
        'weather_checker.backlog.weather_checking.urls', namespace='weather_checking')),
        ]