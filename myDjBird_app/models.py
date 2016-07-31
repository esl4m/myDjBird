#  models.py
#
#  by: Islam Diaa
#       17 Jul 2016
#

from django.db import models
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User

# Create your models here.
fs = FileSystemStorage(location='static/profile_pictures/')
def only_filename(instance, filename):
    return filename

class Users(models.Model):
    user = models.OneToOneField(User)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    profile_picture = models.ImageField(storage=fs, upload_to=only_filename, blank=True, null=True)

    class Meta:
        db_table = 'users'
        verbose_name_plural = "users"


class Timeline(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=250)
    date = models.DateTimeField(db_index=True, auto_now_add=True)

    class Meta:
        db_table = 'timeline'
        verbose_name_plural = "timeline"


class Replies(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status_id = models.ForeignKey(Timeline, on_delete=models.CASCADE)
    content = models.CharField(max_length=250)
    date = models.DateTimeField(db_index=True, auto_now_add=True)

    class Meta:
        db_table = 'replies'
        verbose_name_plural = "replies"


class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status_id = models.ForeignKey(Timeline, on_delete=models.CASCADE)

    class Meta:
        db_table = 'likes'
        verbose_name_plural = "likes"


class Dislikes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status_id = models.ForeignKey(Timeline, on_delete=models.CASCADE)

    class Meta:
        db_table = 'dislikes'
        verbose_name_plural = "dislikes"


class Follow(models.Model):
    following = models.ForeignKey(User, related_name="who_follows")
    follower = models.ForeignKey(User, related_name="who_is_followed")
    follow_time = models.DateTimeField(db_index=True, auto_now_add=True)

    class Meta:
        db_table = 'Follow'
        verbose_name_plural = "Follow"

