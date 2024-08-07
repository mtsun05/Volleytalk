from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    body = models.CharField(max_length=700, null=False)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE, default=Post)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False)
    body = models.TextField(max_length=700, null=False)
    likes = models.IntegerField(blank=True, default=0)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body