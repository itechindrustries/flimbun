from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=50)
    friends = models.ManyToManyField(User,related_name='friends', blank=True)
    insta = models.CharField(max_length=50)
    github = models.CharField(max_length=50)
    twitter = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.user.username} Profile'


class message(models.Model):
    url = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    read = models.IntegerField(default=0)

    def __str__(self):
        return self.author.username
        
class Group(models.Model):
    group_url = models.CharField(max_length=200)
    name = models.CharField(max_length=50)
    topic = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    user = models.ManyToManyField(User, related_name='user', blank=True)

    def __str__(self):
        return f"{self.group_url}"