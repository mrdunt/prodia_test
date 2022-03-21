from django.urls import path

from weather_checker.backlog.auth.views import (
    login_backlog, logout_backlog
)


app_name = 'auth'

urlpatterns = [
    path('login', login_backlog, name='login'),
    path('logout', logout_backlog, name='logout'),
]
