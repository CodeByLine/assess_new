from django.shortcuts import render, get_object_or_404
from blog.models import Post, Comment
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Count
from django.contrib.auth.models import User
from django.conf import settings
# from accounts.models import User

def index(request):
    # pass
    post_list = Post.objects.all()
    num_posts = Post.objects.count()
    num_comments = Comment.objects.count()
    comment_list = Comment.objects.all()

    # # The 'all()' is implied by default.
    # num_authors = Author.objects.count()
    # num_commenters = Commenter.objects.count()

    #SESSION
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    
    context = {
        'num_posts': num_posts,
        'num_comments': num_comments,
        # 'num_authors': num_authors,
    #     'num_commenters': num_commenters,
        'num_visits': num_visits,  #SESSION
        'post_list' : post_list,
        # 'comments' : comments,
    }

    # # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


#####POST
class PostListView(generic.ListView):
    pass
    model = Post
    post_list = Post.objects.all()

    context_vars = {
    #     'num_posts': num_posts,
    #     'num_authors': num_authors,
        'post_list' : post_list,
    #     'num_comments' : num_comments,
    #     'num_commenters' : Commenter.objects.count(),
    }
    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context.update(PostListView.context_vars)
        return context

class PostDetailView(generic.DetailView):
    # pass
    model = Post

    def post_detail_view(request, primary_key):
        post = get_object_or_404(Post, pk=primary_key)
        
        post.author = User.objects.filter(id=post.author.id)
        return render(request, 'post_detail.html', context={'post': post})


    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        # post_comments = Comment.objects.filter(id==kwargs)
    #     num_comments = Comment.objects.filter(
    #         post_connected=self.get_object)).count()
    #     post_connected = Comment.objects.filter(
    #         post_connected=self.get_object()).order_by('-comment_created_at')
    #     data['comments'] = post_connected
        
        return data

##### AUTHOR
class AuthorListView(generic.ListView):
    # pass
    model = User
    template = 'auth/user_list.html'
    authors = User.objects.all()
    num_authors=User.objects.count()
    num_posts = Post.objects.count()
    # def get_authors(self, **kwargs):
    #     authors = User.objects.filter()
    context_vars = {
        'authors' : authors,
        'num_authors' : num_authors,
        'num_posts' : num_posts,
    }

    def get_context_data(self, **kwargs):
        context = super(AuthorListView, self).get_context_data(**kwargs)
        context.update(AuthorListView.context_vars)
        return context

class AuthorDetailView(generic.DetailView):
    # pass
    model = User
    template = 'auth/user_detail.html'
    authors = User.objects.all()
    context_object_name = 'author'
    context = {
        'authors' : authors,
    }
        
# https://www.reddit.com/r/django/comments/okxt25/how_do_i_extract_authors_posts_in_viewspy_django/h5bhrzf?utm_source=share&utm_medium=web2x&context=3
    def author_detail_view(request, primary_key):
        author = get_object_or_404(User, pk=primary_key)
        author_posts = Post.objects.filter(pk='author_id')

        return render(request, 'auth/author_detail.html', context={'author_post': author_post})

    # def get_queryset(self):
    #     """Return queryset """
    #     return User.objects.order_by('id')

    # def get_author_posts(self):
    #     author_posts = Post.objects.filter_by('author_id')
    #     return author_posts

    # def get_context_data(self, **kwargs):
    #     context = super(AuthorDetailView, self).get_context_data(**kwargs)
    
    #     return context

# class AuthorDetailView(generic.DetailView):
#     # view goes to /auth/user_detail
#     # pass
#     model = User
#     context_object_name = 'author'
#     template = 'auth/user_detail.html'

#     def get_author(request, **kwargs):
        # author = get_object_or_404(User, **kwargs == id)
        # author_posts = get_object_or_404(Post, author.id == id)

        # context = {
        #     'author' : author,
        #     'author_posts' : author_posts,
        # }
        # return context
    # def get_queryset(request, **kwargs):
        """Return queryset """
        # author = User.objects.filter(**kwargs)
        # if author.posts is not None:
        #     author_posts = author.posts.all()
        #     return author_posts
        

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
        
    #     return context
    

##### CRUD-POST
class PostCreateView(generic.CreateView):
# class PostCreate(LoginRequiredMixin, CreateView):
    pass
    model = Post
    # fields = ['post_title', 'description']
    # author = request.user

class PostUpdate(generic.UpdateView):
    pass
# class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    #fields = '__all__' # Not recommended (potential security issue if more fields added)

class PostDelete(generic.DeleteView):
# class PostDelete(LoginRequiredMixin, DeleteView):
    pass
    model = Post
    success_url = reverse_lazy('blogs')


##### CRUD-COMMENT
# class CommentCreate(generic.CreateView):
# class CommentCreate(LoginRequiredMixin, CreateView):
    # model = Comment
    # fields = ['comment_title', 'comment_text']


# class CommentUpdate(generic.UpdateView):
# class CommentUpdate(LoginRequiredMixin, UpdateView):
    # model = Comment
    #fields = '__all__' # Not recommended (potential security issue if more fields added)

# class CommentDelete(generic.DeleteView):
# class CommentDelete(LoginRequiredMixin, DeleteView):
    # model = Comment
    # success_url = reverse_lazy('blogs')



