from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView
from accounts.models import CustomUser
from .forms import CustomUserCreationForm

# https://learndjango.com/tutorials/django-custom-user-model

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

##### AUTHOR
class AuthorListView(generic.ListView):
#     pass
    model = CustomUser
    # model = Author
    template = 'author_list.html'
    authors = CustomUser.objects.all()