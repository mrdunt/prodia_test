from typing import Any

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models


class CustomUserManager(UserManager):

    def create_user(self, email: str, password: str, type=None, **extra_fields: Any):
        """
        Creates and saves a User with the email and mobile_number.
        """
        user = self.model(email=email, is_superuser=False, is_active=True, is_staff=True,
                          **extra_fields)
        if password:
            user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email=email, password=password, **extra_fields)
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True
        user.name = user.email
        user.save(using=self._db)
        return user


class WeatherCheckerUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255)
    email = models.EmailField('email address', unique=True, max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    objects = CustomUserManager()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
