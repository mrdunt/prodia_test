from django.urls import path, include

app_name = 'backlog'

urlpatterns = [
    path('areas/', include(
        'weather_checker.backlog.areas.urls', namespace='areas')),
        ]