#  admin.py
#
#  by: Islam Diaa
#       17 Jul 2016
#

from django.contrib import admin
from .models import Users, Timeline, Replies, Likes, Dislikes, Follow

# Register your models here.
class UsersAdmin(admin.ModelAdmin):
    pass

class TimelineAdmin(admin.ModelAdmin):
    pass

class ReplyAdmin(admin.ModelAdmin):
    pass

class LikesAdmin(admin.ModelAdmin):
    pass

class DislikesAdmin(admin.ModelAdmin):
    pass

class FollowAdmin(admin.ModelAdmin):
    pass

admin.site.register(Users, UsersAdmin)
admin.site.register(Timeline, TimelineAdmin)
admin.site.register(Replies, ReplyAdmin)
admin.site.register(Likes, LikesAdmin)
admin.site.register(Dislikes, DislikesAdmin)
admin.site.register(Follow, FollowAdmin)
