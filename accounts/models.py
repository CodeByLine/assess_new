from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username
        
        
# post_connected =  models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE, default=None, null=True)