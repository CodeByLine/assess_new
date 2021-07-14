from django.shortcuts import render, get_object_or_404
from blog.models import Post, Author, Commenter, Comment
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy


def index(request):
    
    post_list = Post.objects.all()
    # Generate counts of some of the main objects
    num_posts = Post.objects.all().count()
    num_comments = Comment.objects.all().count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()
    num_commenters = Commenter.objects.count()

    #SESSION
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_posts': num_posts,
        'num_comments': num_comments,
        'num_authors': num_authors,
        'num_commenters': num_commenters,
        'num_visits': num_visits,  #SESSION
        'post_list' : post_list,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class PostListView(generic.ListView):
    pass


class PostDetailView(generic.DetailView):
    model = Post
    

class AuthorListView(generic.ListView):
    model = Author
    


class AuthorDetailView(generic.DetailView):
    model = Author
    