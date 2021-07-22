from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.conf import settings
from . import views

# from accounts.models import CustomUser
# from .forms import CustomUserCreationForm

# https://learndjango.com/tutorials/django-custom-user-model

class SignUpView(CreateView):
    pass
    # form_class = CustomUserCreationForm
    # success_url = reverse_lazy('login')
    # template_name = 'registration/signup.html'

##### AUTHOR
class AuthorListView(generic.ListView):
    # pass
    model = User
    # template = 'blog/author_list.html'
    authors = User.objects.all()
    num_authors=User.objects.count()
    # num_posts = Post.objects.count()
    # def get_authors(self, **kwargs):
    #     authors = User.objects.filter()
    context_vars = {
        'authors' : authors,
        'num_authors' : num_authors,
    #     'num_posts' : num_posts,
    }

    def get_context_data(self, **kwargs):
        context = super(AuthorListView, self).get_context_data(**kwargs)
        context.update(AuthorListView.context_vars)
        return context
    

# class AuthorDetailView(generic.DetailView):
#     # pass
#     model = User
#     authors = User.objects.all()
#     context_object_name = 'author'
#     context = {
#         'authors' : authors,
#     }

#     def get_queryset(self):
#         """Return queryset """
#         return User.objects.order_by('id')

#     def get_context_data(self, **kwargs):
#         context = super(AuthorDetailView, self).get_context_data(**kwargs)
    
#         return context