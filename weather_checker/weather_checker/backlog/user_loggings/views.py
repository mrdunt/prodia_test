import json

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from weather_checker.apps.user_loggings.models import UserLogging
from weather_checker.backlog.decorators import login_required
from weather_checker.utils import PaginatorPage

@login_required
def index(request):
    user_loggings = UserLogging.objects.all()
    paginator = PaginatorPage(user_loggings, request.GET.get('page', 1), step=20)  # type: ignore

    context = {
        'title': 'User Logging',
        'user_loggings': paginator.objects,
        'paginator': paginator,
        'active_tab': 'user_logging',
        'user': request.user,
    }
    return render(request, 'user_loggings/index.html', context)
