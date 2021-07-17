from django.contrib import admin
from .models import Author, Post, Comment, Commenter
 
# "should not define a __str__ in admin.py. The ModelAdmin itself does not determine how a model object is formatted, this is what the model class does"
# https://stackoverflow.com/a/68411106/5965865

admin.site.register(Post) 
# def __str__(self):
#     return self.title

admin.site.register(Author)
#def __str__(self):
#    return self.author_username

admin.site.register(Comment)
#def __str__(self):
#        return self.comment_title

admin.site.register(Commenter)
#def __str__(self):
#    return self.commenter_username

