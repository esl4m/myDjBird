#  urls.py
#
#  by: Islam Diaa
#       18 Jul 2016
#

from django.conf.urls import url
from . import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^home/$', views.home, name='home'),
    url(r'^about', views.about, name='about'),
    url(r'^list_users', views.list_users, name='list_users'),
    url(r'^show_profile', views.show_profile, name='show_profile'),
    url(r'^accounts/register/$', views.register_user, name='register'),
    url(r'^accounts/register/complete/$', views.register_success, name='registration_complete'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', views.logout_page, name='logout'),
    # url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': ''}),
    # url(r'^accounts/loggedin/$', views.loggedin, name='loggedin'),
    url(r'^post_tweet/$', views.post_update, name='post_tweet'),
    url(r'^view_update/$', views.view_update, name='view_update'),
]