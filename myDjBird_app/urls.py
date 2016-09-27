#  urls.py
#
#  by: Islam Diaa
#       18 Jul 2016
#

from django.conf.urls import url
from . import views, api_views
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about', views.about, name='about'),
    url(r'^list_users', views.list_users, name='list_users'),
    url(r'^post_reply/(?P<status_id>\w+)/$', views.post_reply, name='post_reply'),
    url(r'^post_delete/(?P<status_id>\w+)/$', views.post_delete, name='post_delete'),
    url(r'^show_profile', views.show_my_profile, name='show_profile'),
    url(r'^accounts/register/$', views.register_user, name='register'),
    url(r'^accounts/register/complete/$', views.register_success, name='registration_complete'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^post_tweet/$', views.post_update, name='post_tweet'),
    url(r'^view_user_profile/(?P<user_id>\w+)/$', views.view_user_profile, name='view_user_profile'),
    url(r'^search_users/(?P<user_name>\w+)/$', views.search_users, name='search_users'),  # search_users
    # url(r'^search_tweets/(?P<status_content>\w+)/$', views.search_tweets, name='search_tweets'),  # search_tweets
    url(r'^search_tweets/?$', views.search_tweets, name='search_tweets'),  # search_tweets
    url(r'^post_like/(?P<status_id>\w+)/$', views.post_like, name='post_like'),
    url(r'^post_dislike/(?P<status_id>\w+)/$', views.post_dislike, name='post_dislike'),
    url(r'^view_post/(?P<status_id>\w+)/$', views.view_post, name='view_post'),
    url(r'^follow/(?P<user_id>\w+)/$', views.follow, name='follow'),
    url(r'^unfollow/(?P<user_id>\w+)/$', views.unfollow, name='unfollow'),
    url(r'^accounts/logout/$', views.logout_page, name='logout'),

    url(r'^api/users/$', api_views.UsersList.as_view()),
    url(r'^api/timeline/$', api_views.TimelineList.as_view()),
    url(r'^api/users/(?P<pk>[0-9]+)/$', api_views.UsersDetail.as_view()),
    url(r'^api/timeline/(?P<pk>[0-9]+)/$', api_views.TimelineDetail.as_view()),

    url(r'^api/token-auth/', 'rest_framework.authtoken.views.obtain_auth_token'),
    # http http://127.0.0.1:8000/myDjBird_app/api/token-auth/ username='USERNAME' password='PASSWORD'

    url(r'^api/authview/', api_views.AuthView.as_view()),
    # http http://127.0.0.1:8000/myDjBird_app/api/authview/ 'Authorization: Token YOUR_TOKEN'

    url(r'^api/list_users/', api_views.UsersList.as_view()),
    url(r'^api/timeline/', api_views.TimelineList.as_view()),
]
