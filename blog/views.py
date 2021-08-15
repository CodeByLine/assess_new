from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post, Comment
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required, permission_required
# from django.db.models import Count
from django.contrib.auth.models import User
# from django.conf import settings
from . forms import PostCreateForm, PostUpdateForm,  CommentForm
from django.core.exceptions import ObjectDoesNotExist



def index(request):
    # pass
    post_list = Post.objects.all()
    num_posts = Post.objects.count()
    num_comments = Comment.objects.count()
    comment_list = Comment.objects.all()

    # # The 'all()' is implied by default.
    num_authors = User.objects.count()
    # num_commenters = Commenter.objects.count()

    #SESSION
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    
    context = {
        'num_posts': num_posts,
        'num_comments': num_comments,
        'num_authors': num_authors,
    #     'num_commenters': num_commenters,
        'num_visits': num_visits,  #SESSION
        'post_list' : post_list,
        # 'comments' : comments,
    }

    # # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


#####POST
class PostListView(generic.ListView):
    # pass
    model = Post
    post_list = Post.objects.all()

    context_vars = {
        'post_list' : post_list,
    }

### Block below isn't needed
    # def get_context_data(self, **kwargs):
    #     context = super(PostListView, self).get_context_data(**kwargs)
    #     context.update(PostListView.context_vars)
    #     return context

### FUNCTION-BASED VIEW - WORKING - DISPLAYS,SAVES,BINDS TO POST
def post_detail(request, pk):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, pk=pk)
    comments = post.comment.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        
        if comment_form.is_valid():    
            comment_form.instance.commenter = request.user      
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post_connected = post
            # Save the commenter   
            # commenter = new_comment.commenter
            commenter = request.POST.get('commenter')
            # Save the comment to the database
            new_comment.save()
            return redirect('/')
    else:
        comment_form = CommentForm()

#below: template's path
    return render(request, 'post_detail.html', {'post': post,
              'comments': comments,
              'new_comment': new_comment,
              'comment_form': comment_form})


### CLASS-BASED VIEW - WORKING - DISPLAYS,SAVES,BINDS TO POST
# class PostDetailView(generic.DetailView):
#     pass
    # model = Post
    # form_class = CommentForm

    # def get(self, request, *args, **kwargs):
    #     try:
    #         self.object = self.get_object()
    #     except ObjectDoesNotExist:
    #         return redirect('blogs')
        
    #     context = self.get_context_data(object=self.object)
        
    #     return self.render_to_response(context)


    # def post(self, request, *args, **kwargs):
    #     comment_form = self.form_class(request.POST)
    #     post = get_object_or_404(Post, **kwargs)   
    #     new_comment = None
    #     if self.request.user.is_authenticated:
    #         comment_form = CommentForm(data=request.POST)
    #         new_comment = comment_form.save(commit=False)
    #         # Assign the current post to the comment
    #         new_comment.post_connected = post
    #         if comment_form.is_valid():
    #         # Save the commenter         
    #             new_comment.commenter = self.request.user
    #         # Save the comment to the database
    #             new_comment.save()
    #             return redirect('/')
    #         else:
    #             comment_form = CommentForm()
    #         return HttpResponseRedirect('/success/')

    #     return render(request, self.template_name, {'comment_form': comment_form})



    # def get_context_data(self, **kwargs):
    #     data = super().get_context_data(**kwargs)

    # #comments
    #     post_connected = Comment.objects.filter(
    #         post_connected=self.get_object()).filter(active=True).order_by('-comment_created_at')
    #     data['comments'] = post_connected

    # #blank form
    #     if self.request.user.is_authenticated:
    #         comment_form = CommentForm()
    #         data['comment_form'] = CommentForm(instance=self.request.user)

    #     return data        


##### AUTHOR
class AuthorListView(generic.ListView):
    # pass
    model = User
    template = 'auth/user_list.html'
    authors = User.objects.all()
    num_authors=User.objects.count()
    num_posts = Post.objects.count()

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
    # context_object_name = 'author'
        
# https://www.reddit.com/r/django/comments/okxt25/how_do_i_extract_authors_posts_in_viewspy_django/h5bhrzf?utm_source=share&utm_medium=web2x&context=3
    def author_detail_view(request, primary_key):
        author = get_object_or_404(User, pk=primary_key)
        author_posts = Post.objects.filter(pk='author_id')

        return render(request, 'auth/author_detail.html', context={'author_posts': author_posts})

    # def get_queryset(self):
    #     """Return queryset """
    #     return User.objects.order_by('id')

    # def get_author_posts(self):
    #     author_posts = Post.objects.filter_by('author_id')
    #     return author_posts



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
     #   """Return queryset """
        # author = User.objects.filter(**kwargs)
        # if author.posts is not None:
        #     author_posts = author.posts.all()
        #     return author_posts
        

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
        
    #     return context
    

##### CRUD - POST
# class PostCreateView(generic.CreateView):
class PostCreateView(LoginRequiredMixin, CreateView):
    # pass
    model = Post
    form = PostCreateForm
    fields = ['post_title', 'description']
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
            return super().form_valid(form)

            
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form = PostUpdateForm
    template = 'post-update.html'
    fields = ['post_title', 'description']
    success_url = reverse_lazy('blogs')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    # def get_queryset(self):
    #     queryset = super(PostUpdateView, self).get_queryset()
    #     queryset = queryset.filter(author=self.request.user)
    #     return queryset


# class PostDelete(generic.DeleteView):
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    # pass
    model = Post
    success_url = reverse_lazy('blogs')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


##### CRUD - COMMENT

## NOT needed
# class CommentCreateView(LoginRequiredMixin, CreateView):
#     model = Comment
#     form = CommentForm
#     fields = ['comment_title', 'comment']
#     success_url = reverse_lazy('comment_detail')

#     def comment_create_view(request, pk):
#         template_name = 'comment_detail.html'
#         post = get_object_or_404(Post, pk=pk)
#         post.new_comment = None
#         # Comment posted
#         if request.method == 'POST':
#             comment_form = CommentForm(data=request.POST)
#             if comment_form.is_valid():

# #                 # Create Comment object but don't save to database yet
#                 post.new_comment = comment_form.save(commit=False)
# #                 # Assign the current post to the comment
#                 new_comment.post = post
# #                 # Save the comment to the database
#                 new_comment.save()
# #         else:
#             comment_form = CommentForm()

#         return render(request, template_name, {'post': post,
#                     'new_comment': new_comment,
#                     'comment_form': comment_form})


class CommentDetailView(LoginRequiredMixin, UserPassesTestMixin, generic.DetailView):
    model = Comment
    fields = ['comment_title', 'comment_text']
    #fields = '__all__' # Not recommended (potential security issue if more fields added)
    success_url = reverse_lazy('comment-detail')

# Not needed
# class CommentCreate(generic.CreateView):
# class CommentCreateView(LoginRequiredMixin, CreateView):
#     model = Comment
#     form = CommentForm
#     fields = ['comment_title', 'comment']
#     success_url = reverse_lazy('blogs')

#     def get_commenter(request, form):
#         form.instance.commented = request.user
#         return super().form_valid(form)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # context['post'] = self.post_connected
# #         # self.commenter = user
#         return context

#     def get_post(request, slug):
#         post = get_object_or_404(Post, slug=slug)
#         form = CommentCreateForm
#         if form.is_valid():
#             comment = form.save(commit=False)
#             post.post_connected=comment.post
#             comment.commenter.id = request.user.id
#             comment.save()
#             return redirect(request.path)
#         return render(request, 'blog/post_detail.html',{'post': post,'form': form,})

#     def form_valid(request, form):
#         form.instance.commenter = request.user
#         return super().form_valid(form)

# class CommentUpdate(generic.UpdateView):
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    fields = ['comment_title', 'comment_text']
    #fields = '__all__' # Not recommended (potential security issue if more fields added)
    success_url = reverse_lazy('post-detail')

# class CommentDelete(generic.DeleteView):
class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    success_url = reverse_lazy('post-detail')



