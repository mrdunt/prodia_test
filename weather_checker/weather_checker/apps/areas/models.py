from django.db import models

class Province(models.Model):
    name = models.CharField(max_length=100, unique=True)
    lat = models.CharField(max_length=255)
    long = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'province'