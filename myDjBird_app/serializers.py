#  serializers.py
#
#  by: Islam Diaa
#       4 Sep 2016
#

from rest_framework import serializers
from .models import Users, Timeline, Replies

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'email', 'profile_picture')


class TimelineSerializer(serializers.ModelSerializer):
    user = UsersSerializer()

    class Meta:
        model = Timeline
        fields = ('id', 'user', 'content', 'date')

class RepliesSerializer(serializers.ModelSerializer):
    user = UsersSerializer()

    class Meta:
        model = Replies
        fields = ('id', 'user', 'status_id', 'content', 'date')
