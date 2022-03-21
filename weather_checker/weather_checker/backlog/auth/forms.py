from django import forms
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404
from django.urls import reverse

from weather_checker.apps.users.models import WeatherCheckerUser


class LoginAuthForm(AuthenticationForm):
    username = forms.EmailField(label='Email User')

    def __init__(self, *args, **kwargs):
        super(LoginAuthForm, self).__init__(*args, **kwargs)
