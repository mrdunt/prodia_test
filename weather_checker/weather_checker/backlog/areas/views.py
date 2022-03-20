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


def index(request):
    provinces = Province.objects.all()
    paginator = PaginatorPage(provinces, request.GET.get('page', 1), step=20)  # type: ignore

    context = {
        'title': 'Province',
        'provinces': paginator.objects,
        'paginator': paginator,
        'active_tab': 'province',
        'user': request.user,
    }
    return render(request, 'areas/index.html', context)
