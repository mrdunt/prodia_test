import json

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from weather_checker.apps.user_loggings.models import UserLogging
from weather_checker.backlog.weather_checking.forms import CheckWeatherForm
from weather_checker.backlog.decorators import login_required

@login_required
def index(request):
    form = CheckWeatherForm(data=request.POST or None)
    response = None
    if request.method == 'POST':
        if form.is_valid():
            response = form.save()
            if response.get('error'):
                error_message = response.get('message')
                messages.error(request, error_message)
                return redirect('weather_checker:weather_checking:index')
            import pdb; pdb.set_trace()
            UserLogging.objects.create(
                user=request.user,
                result_meta=response
            )
            messages.success(request, "Success Check Weather")
    context = {
        'form': form,
        'active_tab': 'weather_check',
        'weather_info': response
    }
    return render(request, 'weather_checking/index.html', context)
