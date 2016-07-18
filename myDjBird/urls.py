#  urls.py
#
#  by: Islam Diaa
#       17 Jul 2016
#

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^myDjBird_app/', include('myDjBird_app.urls')),
    # url(r'^myDjBird_app/view/view_update.html', 'myDjBird_app.views.view_update', name='view_update'),
    url(r'^admin/', include(admin.site.urls)),
    # # url(r'^$', 'myDjBird.views.index'),
    # url(r'^myDjBird_app/', include('myDjBird_app.urls')),

    # # url(r'^blog/category/(?P<slug>[^\.]+).html', 'myDjBird.myDjBird_app.views.view_category', name='view_blog_category'),
    # # Examples:
    # # url(r'^$', 'myDjBird.views.home', name='home'),
    # # url(r'^blog/', include('blog.urls')),
    #
    # url(r'^admin/', include(admin.site.urls)),
]
