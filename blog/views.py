from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required

def index(request):
    pass
    
    # post_list = Post.objects.all()
    # # Generate counts of some of the main objects
    # num_posts = Post.objects.count()
    # num_comments = Comment.objects.count()

    # # The 'all()' is implied by default.
    # num_authors = Author.objects.count()
    # num_commenters = Commenter.objects.count()

    # #SESSION
    # num_visits = request.session.get('num_visits', 1)
    # request.session['num_visits'] = num_visits + 1

    context = {
    #     'num_posts': num_posts,
    #     'num_comments': num_comments,
    #     'num_authors': num_authors,
    #     'num_commenters': num_commenters,
    #     'num_visits': num_visits,  #SESSION
    #     'post_list' : post_list,
    }

    # # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


#####POST
class PostListView(generic.ListView):
    pass
    model = Post
    # post_list = Post.objects.all()
    # num_posts = Post.objects.count()
    # num_authors = Author.objects.count()
    # num_comments = Comment.objects.all().count()
    # num_commenters = Commenter.objects.count()

    # template_name = 'blog/post_list.html'  # Specify your own template name/location

    # context_vars = {
    #     'num_posts': num_posts,
    #     'num_authors': num_authors,
    #     'post_list' : post_list,
    #     'num_comments' : num_comments,
    #     'num_commenters' : Commenter.objects.count(),
    # }
    # def get_context_data(self, **kwargs):
    #     context = super(PostListView, self).get_context_data(**kwargs)
    #     context.update(PostListView.context_vars)
    #     return context

class PostDetailView(generic.DetailView):
    pass
    model = Post
    # def post_detail_view(request, primary_key):
    #     post = get_object_or_404(Post, pk=primary_key)
    #     post_comments = Comment.objects.filter(post.kwargs['pk'])
    #     post_author = Post.objects.filter(post.author.kwargs['pk'])
    #     return render(request, 'post_detail.html', context={'post': post})

    # def get_context_data(self, **kwargs):
    #     data = super().get_context_data(**kwargs)
    #     num_comments = Comment.objects.filter(
    #         post_connected=self.get_object()).count()
    #     post_connected = Comment.objects.filter(
    #         post_connected=self.get_object()).order_by('-comment_created_at')
    #     data['comments'] = post_connected

    #     return data

##### AUTHOR
class AuthorListView(generic.ListView):
    pass
    # model = Author
    # template = 'author_list.html'
    # authors = Author.objects.all()
    # num_authors=Author.objects.count()
    # num_posts = Post.objects.count()

    # context_vars = {
    #     'authors' : authors,
    #     'num_authors' : num_authors,
    #     'num_posts' : num_posts,
    # }

    # def get_context_data(self, **kwargs):
    #     context = super(AuthorListView, self).get_context_data(**kwargs)
    #     context.update(AuthorListView.context_vars)
    #     return context
    

class AuthorDetailView(generic.DetailView):
    pass
    # model = Author
    # context_object_name = 'author'

    # def author_detail_view(request, primary_key):
    #     author = get_object_or_404(Author, pk=primary_key)
        
    #     return render(request, 'author_detail.html')

# below: Does nothing
    # def get_author_posts(self, **kwargs):
    #     author_posts = Post.objects.filter(self.author.kwargs['pk'])
    #     return author_posts


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     author_posts = Post.objects.filter(author=self.kwargs['pk'])
    #     context['author_posts'] = author_posts
    #     return context
    

##### CRUD-POST
class PostCreateView(CreateView):
# class PostCreate(LoginRequiredMixin, CreateView):
    pass
    model = Post
    # fields = ['post_title', 'description']
    # author = request.user

class PostUpdate(UpdateView):
# class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    #fields = '__all__' # Not recommended (potential security issue if more fields added)

class PostDelete(DeleteView):
# class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blogs')


##### CRUD-COMMENT
# class CommentCreate(CreateView):
# class CommentCreate(LoginRequiredMixin, CreateView):
    # model = Comment
    # fields = ['comment_title', 'comment_text']


# class CommentUpdate(UpdateView):
# class CommentUpdate(LoginRequiredMixin, UpdateView):
    # model = Comment
    #fields = '__all__' # Not recommended (potential security issue if more fields added)

# class CommentDelete(DeleteView):
# class CommentDelete(LoginRequiredMixin, DeleteView):
    # model = Comment
    # success_url = reverse_lazy('blogs')



