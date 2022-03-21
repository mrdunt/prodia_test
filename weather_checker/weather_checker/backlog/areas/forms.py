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

    def __init__(self, instance, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance = instance
        if instance:
            self.fields['name'].initial = instance.name
            self.fields['latitude'].initial = instance.lat
            self.fields['longitude'].initial = instance.long


    def clean(self):
        data = super().clean()
        return data

    def save(self):
        name = self.cleaned_data['name']
        lat = self.cleaned_data['latitude']
        long = self.cleaned_data['longitude']
        if self.instance:
            self.instance.name = name
            self.instance.lat = lat
            self.instance.long = long
            province = self.instance.save()
            return province

        else:
            province = Province.objects.create(
                name=name,
                lat=lat,
                long=long
            )
            return province
