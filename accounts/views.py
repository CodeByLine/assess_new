from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.conf import settings
from . import views
from blog.models import Post, Comment
from blog.views import AuthorDetailView, AuthorListView
from . forms import UserCreationForm #UserChangeForm

class SignUpView(CreateView):
    # pass
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

##### AUTHOR
# class AuthorListsView(generic.ListView):
#     # pass
#     model = User
#     # template = 'blog/author_list.html'
#     authors = User.objects.all()
#     num_authors=User.objects.count()
#     # num_posts = Post.objects.count()
#     # def get_authors(self, **kwargs):
#     #     authors = User.objects.filter()
#     context_vars = {
#         'authors' : authors,
#         'num_authors' : num_authors,
#     #     'num_posts' : num_posts,
#     }

#     def get_context_data(self, **kwargs):
#         context = super(AuthorListsView, self).get_context_data(**kwargs)
#         context.update(AuthorListsView.context_vars)
#         return context
    

# # class AuthorDetailsView(generic.DetailView):
# #     # pass
# #     model = User
# #     authors = User.objects.all()
# #     num_authors=User.objects.count()
# #     context_object_name = 'author'
# #     author_posts = Post.objects.filter(author_id=author.id)
# #     context2 = {
# #         'authors' : authors,
# #         'num_authors' : num_authors,
# #     }

# #     # def get_queryset(self):
# #     #     """Return queryset """
# #     #     return User.objects.order_by('id')

# #     def get_context_data(self, **kwargs):
# #         context = super(AuthorDetailsView, self).get_context_data(**kwargs)
# #         context.update(AuthorDetailsView.context2)
# #         return context
    
# #         return context