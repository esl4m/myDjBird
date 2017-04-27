#  urls.py
#
#  by: Islam Diaa
#       17 Jul 2016
#

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^myDjBird_app/', include('myDjBird_app.urls')),
]

