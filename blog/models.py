from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
from django.db.models import Count

# User = settings.AUTH_USER_MODEL

class Post(models.Model):
    post = models.TextField(max_length=1000)
    post_title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    post_created_at = models.DateTimeField(auto_now_add=True)
    post_updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)

    # https://learndjango.com/tutorials/django-best-practices-referencing-user-model
# from django.contrib.auth.models import User
# from django.conf import settings

    # author = models.ForeignKey(
    #   settings.AUTH_USER_MODEL, related_name="posts", 
    #   on_delete=models.CASCADE
    # )
    
    @property
    def num_comments(self):
        return Comment.objects.filter(post_connected=self).count()


    # @property
    # def post_comments(self):
    #     return Comment.objects.filter(post_connected=self)

    def __str__(self):
        return f'{self.author or ""} – {self.post_title[:40]}'

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])

    def get_absolute_url(self):
        return "/blog/{}/".format(self.pk)

    # Metadata
    class Meta:
        ordering = ['-post_created_at']
    
    # def get_author():
    #     a = CustomUser()
    #     name = a.get_username() # author instance
        # https://stackoverflow.com/questions/58891302/django-customuser-function
    
# class TimeStampMixin(models.Model):
#     # see https://stackoverflow.com/a/57971729/5965865
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         abstract = True


class Comment(models.Model):
     # also see https://stackoverflow.com/a/57971729/5965865

    comment_title = models.CharField(max_length=100)
    comment = models.TextField(max_length=1000)
    comment_created_at = models.DateTimeField(auto_now_add=True)
    comment_updated_at = models.DateTimeField(auto_now=True)
    
    commenter = models.ForeignKey(User, related_name="commented", null=True, blank=True, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    # commenter = models.ForeignKey(
    #   settings.AUTH_USER_MODEL, 
    #   on_delete=models.CASCADE
    # )

    post_connected =  models.ForeignKey(Post, related_name='comment', on_delete=models.CASCADE, default=None, null=True) #

    class Meta:
        ordering = ['comment_created_at']

    def __str__(self):
        return str(self.commenter) + ' :  ' + self.comment_title[:40]

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)]) 


