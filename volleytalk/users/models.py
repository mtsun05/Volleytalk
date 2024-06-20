from django.db import models

# Create your models here.
class User(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    pfp = models.ImageField()

    def __str__(self):
        return self.fname + self.lname