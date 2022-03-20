from django.db import models


class UserLogging(models.Model):
    user = models.ForeignKey('users.WeatherCheckerUser', related_name="userlogging",
                            on_delete=models.CASCADE)
    result_meta = models.JSONField(default={})
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
