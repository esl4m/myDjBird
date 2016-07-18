#  urls.py
#
#  by: Islam Diaa
#       18 Jul 2016
#

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register_user/$', views.register_user, name='index'),
    # url(r'^add_user/$', views.add_user, name='add_user'),
    url(r'^view_update/$', views.view_update, name='view_update'),
]