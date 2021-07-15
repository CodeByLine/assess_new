from django.db import models
from django.urls import reverse
from datetime import date


class Post(models.Model):
    post_title = models.CharField(max_length=100, help_text='Enter a title')
    post_created_at = models.DateTimeField(auto_now_add=True)
    post_updated_at = models.DateTimeField(auto_now=True)

    # author = models.ForeignKey('Author', related_name='author', on_delete=models.SET_DEFAULT, default=None, null=True)
    author = models.ForeignKey('Author', on_delete=models.SET_DEFAULT, default=None, null=True)

    description = models.TextField(max_length=1000, help_text='Enter a brief description of this post')


    @property
    def num_comments(self):
        return Comment.objects.filter(post_connected=self).count()

    @property
    def post_comments(self):
        return Comment.objects.filter(post_connected=self)

    def __str__(self):
        return self.author.author_username + ', ' + self.post_title[:40]

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])

    # Metadata
    class Meta:
        ordering = ['-post_created_at']
    
class TimeStampMixin(models.Model):
    # see https://stackoverflow.com/a/57971729/5965865
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Author(models.Model):
    # see https://stackoverflow.com/a/57971729/5965865
    author_first_name = models.CharField(max_length=30, help_text='Enter first name')
    author_last_name = models.CharField(max_length=30, help_text='Enter last name')
    author_username = models.CharField(max_length=20)

    def __str__(self):
        return self.author_username 
        
    #useless
    # @property
    # def author_posts(self):
    #     return Post.objects.filter(post_connected=self)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

class Comment(TimeStampMixin):
     # see https://stackoverflow.com/a/57971729/5965865

    comment_title = models.CharField(max_length=100, help_text='Enter a title')
    comment_text = models.TextField(max_length=1000, help_text='Write your comment here')
    comment_created_at = models.DateTimeField(auto_now_add=True)
    comment_updated_at = models.DateTimeField(auto_now=True)
    commenter = models.ForeignKey('Commenter', on_delete=models.SET_DEFAULT, default=None, null=True)

    #useless
    #post = models.ForeignKey('Post', on_delete=models.SET_DEFAULT, default=None, null=True) #useless

    post_connected =  models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE, default=None, null=True)

    class Meta:
        ordering = ['comment_created_at']

    def __str__(self):
        return str(self.commenter) + ' :  ' + self.comment_title[:40]
      

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])

class Commenter(models.Model):
    commenter_username = models.CharField(max_length=20)
    
    def __str__(self):
        return self.commenter_username