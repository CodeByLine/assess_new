# https://learndjango.com/tutorials/django-custom-user-model

# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
from django.db.models import Count

class CustomUser(AbstractUser):
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True) # check this for login email purposes
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username
