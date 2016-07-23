#  models.py
#
#  by: Islam Diaa
#       17 Jul 2016
#

from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    # pic = models.ImageField(upload_to=get_upload_file_name,
    #                         width_field="width_field",
    #                         height_field="height_field",
    #                         null=True,
    #                         blank=True,
    #                         verbose_name=("Profile Picture")
    #                         )

    class Meta:
        db_table = 'users'
        verbose_name_plural = "users"


class Timeline(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    content = models.CharField(max_length=250)
    date = models.DateTimeField(db_index=True, auto_now_add=True)
    # content_type = models.CharField(max_length=250, db_index=True) # status_update / reply
    # likes_count = models.IntegerField()
    # dislikes_count = models.IntegerField()

    class Meta:
        db_table = 'timeline'
        verbose_name_plural = "timeline"


class Reply(models.Model):
    status_id = models.ForeignKey(Timeline, on_delete=models.CASCADE)
    content = models.CharField(max_length=250)
    date = models.DateTimeField(db_index=True, auto_now_add=True)

    class Meta:
        db_table = 'reply'
        verbose_name_plural = "replies"


class Likes(models.Model):
    status_id = models.ForeignKey(Timeline, on_delete=models.CASCADE)
    likes_count = models.IntegerField()

    class Meta:
        db_table = 'likes'
        verbose_name_plural = "likes"


class Dislikes(models.Model):
    status_id = models.ForeignKey(Timeline, on_delete=models.CASCADE)
    dislikes_count = models.IntegerField()

    class Meta:
        db_table = 'dislikes'
        verbose_name_plural = "dislikes"


class IFollow(models.Model):
    user_me = models.ForeignKey(Users, related_name='+', on_delete=models.CASCADE)
    user_i_follow = models.ForeignKey(Users, on_delete=models.CASCADE)

    class Meta:
        db_table = 'iFollow'
        verbose_name_plural = "iFollow"


class FollowMe(models.Model):
    user_followed_me = models.ForeignKey(Users, related_name='+', on_delete=models.CASCADE)
    user_me = models.ForeignKey(Users, on_delete=models.CASCADE)

    class Meta:
        db_table = 'followMe'
        verbose_name_plural = "followMe"
