from django.contrib import admin
from .models import Post, Comment
 
# "should not define a __str__ in admin.py. The ModelAdmin itself does not determine how a model object is formatted, this is what the model class does"
# https://stackoverflow.com/a/68411106/5965865

admin.site.register(Post) 
# def __str__(self):
#     return self.title

# admin.site.register(Comment) 


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_title', 'comment', 'comment_created_at', 'commenter')
    list_filter = ('comment_title', 'commenter')
    search_fields = ('comment_title', 'comment')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)