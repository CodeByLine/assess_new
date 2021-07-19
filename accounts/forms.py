## https://learndjango.com/tutorials/django-custom-user-model


# https://www.codingforentrepreneurs.com/blog/how-to-create-a-custom-django-user-model

# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class UserCreationForm(UserCreationForm):
    pass
    # class Meta:
    #     model = User
    #     fields = ('email')

class UserChangeForm(UserChangeForm):
    pass
    # class Meta:
    #     model = User
    #     fields = ('email')