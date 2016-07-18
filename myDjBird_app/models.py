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
        db_table = 'Users'


class Timeline(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    content = models.CharField(max_length=250)
    date = models.DateTimeField(db_index=True, auto_now_add=True)
    # content_type = models.CharField(max_length=250, db_index=True) # status_update / reply
    # likes_count = models.IntegerField()
    # dislikes_count = models.IntegerField()

    class Meta:
        db_table = 'Timeline'


class Reply(models.Model):
    status_id = models.ForeignKey(Timeline, on_delete=models.CASCADE)
    content = models.CharField(max_length=250)
    date = models.DateTimeField(db_index=True, auto_now_add=True)

    class Meta:
        db_table = 'Reply'


class Likes(models.Model):
    status_id = models.ForeignKey(Timeline, on_delete=models.CASCADE)
    likes_count = models.IntegerField()

    class Meta:
        db_table = 'Likes'


class Dislikes(models.Model):
    status_id = models.ForeignKey(Timeline, on_delete=models.CASCADE)
    dislikes_count = models.IntegerField()

    class Meta:
        db_table = 'Dislikes'


class IFollow(models.Model):
    user_me = models.ForeignKey(Users, related_name='+', on_delete=models.CASCADE)
    user_i_follow = models.ForeignKey(Users, on_delete=models.CASCADE)

    class Meta:
        db_table = 'IFollow'


class FollowMe(models.Model):
    user_followed_me = models.ForeignKey(Users, related_name='+', on_delete=models.CASCADE)
    user_me = models.ForeignKey(Users, on_delete=models.CASCADE)

    class Meta:
        db_table = 'FollowMe'
