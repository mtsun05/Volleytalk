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
    


class Ranking(models.Model):
    team = models.CharField(max_length=200)
    score = models.CharField(max_length=200)
    qualified = models.BooleanField(default=False)