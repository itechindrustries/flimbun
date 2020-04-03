from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=50, blank=True)
    friends = models.ManyToManyField(User,related_name='friends', blank=True)
    insta = models.CharField(max_length=50, blank=True)
    github = models.CharField(max_length=50, blank=True)
    twitter = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'


class message(models.Model):
    url = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.author.username
        
class Group(models.Model):
    group_url = models.CharField(max_length=200)
    name = models.CharField(max_length=50)
    topic = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    user = models.ManyToManyField(User, related_name='user', blank=True)
    last_msg_groups = models.TextField(blank=True)
    time_groups = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    unread_groups = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return f"{self.group_url}"

class fchat(models.Model):
    fuser = models.ManyToManyField(User, related_name='fuser', blank=True)
    furl = models.CharField(max_length=200)
    last_msg_single = models.TextField(blank=True)
    time_single = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    unread_single = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return f"{self.furl}"


@receiver(post_save, sender=User)
def user_is_created (sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user=instance)
    else:
        instance.profile.save()