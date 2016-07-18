#  admin.py
#
#  by: Islam Diaa
#       17 Jul 2016
#

from django.contrib import admin
from .models import Users, Timeline, Reply, Likes, Dislikes, IFollow, FollowMe

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

class IFollowAdmin(admin.ModelAdmin):
    pass

class FollowMeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Users, UsersAdmin)
admin.site.register(Timeline, TimelineAdmin)
admin.site.register(Reply, ReplyAdmin)
admin.site.register(Likes, LikesAdmin)
admin.site.register(Dislikes, DislikesAdmin)
admin.site.register(IFollow, IFollowAdmin)
admin.site.register(FollowMe, FollowMeAdmin)
