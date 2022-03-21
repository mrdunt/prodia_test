import json
import requests

from django import forms
from django.conf import settings
from django.utils import timezone

from rest_framework import status

from weather_checker.apps.areas.models import Province

class CreateAreaForm(forms.Form):
    name = forms.CharField()
    latitude = forms.CharField()
    longitude = forms.CharField()

    def clean(self):
        data = super().clean()
        return data

    def save(self):
        name = self.cleaned_data['name']
        lat = self.cleaned_data['latitude']
        long = self.cleaned_data['longitude']
        province = Province.objects.create(
            name=name,
            lat=lat,
            long=long
        )
        return province
