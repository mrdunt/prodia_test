import json

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from weather_checker.apps.areas.models import Province
from weather_checker.utils import PaginatorPage
from weather_checker.backlog.weather_checking.forms import CheckWeatherForm


def index(request):
    form = CheckWeatherForm(data=request.POST or None)
    weather_info = {}
    if request.method == 'POST':
        if form.is_valid():
            response = form.save()
            if response.get('error'):
                error_message = response.get('message')
                messages.error(request, error_message)
                return redirect('weather_checker:weather_checking:index')
            weather_info = {
                "lat" : response.get('lat'),
                "long": response.get('lon'),
                "timezone": response.get('timezone'),
                "pressure": response.get('current').get('pressure'),
                "humidity": response.get('current').get('humidity'),
                "wind_speed": response.get('current').get('wind_speed'),
                "main": response.get('current').get('weather')[0].get('main'),
                "description": response.get('current').get('weather')[0].get('description'),
            }
            messages.success(request, "Success Check Weather")
    context = {
        'form': form,
        'active_tab': 'products',
        'active_sub_tab': 'product',
        'weather_info': weather_info
    }
    return render(request, 'weather_checking/index.html', context)
