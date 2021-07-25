## https://learndjango.com/tutorials/django-custom-user-model


# https://www.codingforentrepreneurs.com/blog/how-to-create-a-custom-django-user-model

# blog/forms.py
# from django import forms
from django.forms import ModelForm
from .models import Post, Comment
from django.contrib.auth.models import User

class PostCreateForm(ModelForm):

    class Meta:
        model = Post
        fields = ['post_title', 'description', 'author']

class PostUpdateForm(ModelForm):
    # pass
    class Meta:
        model = Post
        fields = ['post_title', 'description', 'author']