import json
import requests

from django import forms
from django.conf import settings
from django.utils import timezone

from rest_framework import status

class CheckWeatherForm(forms.Form):

    latitude = forms.CharField()
    longitude = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        data = super().clean()
        return data

    def save(self):
        lat = self.cleaned_data['latitude']
        long = self.cleaned_data['longitude']
        api_key = settings.API_KEY
        url = settings.OPEN_WEATHER_MAP_URL
        request_params = {
            'lat': lat,
            'lon': long,
            'appid': api_key,
        }
        response_json = None
        weather_info = None
        response = requests.get(url=url,
                                     params=request_params)
        response_json = json.loads(response.content.decode('utf-8'))
        if response.status_code != status.HTTP_200_OK:
            response_json = {
                "status_code": response.status_code,
                "error": "error_checking",
                "message": response_json.get('message')
            }

        weather_info = {
                "lat" : response_json.get('lat'),
                "long": response_json.get('lon'),
                "timezone": response_json.get('timezone'),
                "pressure": response_json.get('current').get('pressure'),
                "humidity": response_json.get('current').get('humidity'),
                "wind_speed": response_json.get('current').get('wind_speed'),
                "main": response_json.get('current').get('weather')[0].get('main'),
                "description": response_json.get('current').get('weather')[0].get('description'),
            }
        return weather_info