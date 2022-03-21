import json

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from weather_checker.apps.areas.models import Province
from weather_checker.backlog.areas.forms import CreateAreaForm
from weather_checker.backlog.decorators import login_required
from weather_checker.utils import PaginatorPage


@login_required
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


@login_required
def create_area(request):
    form = CreateAreaForm(data=request.POST or None, instance=None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Area telah berhasil dibuat')
            return redirect('backlog:areas:index')
    context = {
        'title': 'Create Area',
        'form': form,
        'active_tab': 'province',
    }
    return render(request, 'areas/area.html', context)


@login_required
def update_area(request, id):
    existing_province = get_object_or_404(Province, id=id)
    form = CreateAreaForm(data=request.POST or None, instance=existing_province)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Area telah berhasil diupdate')
            return redirect('backlog:areas:index')
    context = {
        'form': form,
        'active_tab': 'province',
        'title': 'Update Province',
    }
    return render(request, 'areas/area.html', context)
