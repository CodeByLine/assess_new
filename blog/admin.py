from django.contrib import admin
from .models import Author, Post, Comment, Commenter


admin.site.register(Post) 
def __str__(self):
    return self.title

admin.site.register(Author)
def __str__(self):
    return self.author_username

admin.site.register(Comment)
def __str__(self):
        return self.comment_title

admin.site.register(Commenter)
def __str__(self):
    return self.commenter_username
