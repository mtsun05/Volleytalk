from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    body = models.CharField(max_length=700, null=True)
    likes = models.IntegerField(blank=True, default=0)
    post_date = models.DateTimeField(blank=True, default=timezone.now)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    body = models.CharField(max_length=700, null=True)
    likes = models.IntegerField(blank=True, default=0)
    post_date = models.DateTimeField(blank=True, default=timezone.now)