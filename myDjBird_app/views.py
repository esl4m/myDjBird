#  views.py
#
#  by: Islam Diaa
#       17 Jul 2016
#

from django.shortcuts import render, redirect
from .models import Users, Timeline, Reply, Likes, Dislikes, FollowMe, IFollow
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    return render_to_response('index.html', {
        'timeline': Timeline.objects.all()[:5]
    })

def view_update(request):
    return render_to_response('view_update.html', {
        'update': get_object_or_404(Timeline)
    })

def register_user(request):
    if request.method == 'POST':
        form = Users(request.POST)
        if form.is_valid():
            new_user = Users(username=request.POST['username'],
                             password=request.POST['password'],
                             email=request.POST['email'],
                             profile_picture=request.POST['profile_picture'])
            new_user.save()
            return HttpResponseRedirect(reverse('index.html'))
    else:
        form = Users()
    return render(request, 'register.html', {'form': form})

# def add_user(request):
#     new_case = Users(username=request.POST['username'],
#                      password=request.POST['password'],
#                      email=request.POST['email'],
#                      profile_picture=request.POST['profile_picture'])
#     new_case.save()
#     return HttpResponseRedirect(reverse('index'))

def post_update(request):
    form = Timeline(request.POST)
    if request.method == 'POST' and form.is_valid():
        new_update = Timeline(user_id = request.POST['user_id'],
                              content = request.POST['content'])
        new_update.save()
        return HttpResponseRedirect(reverse('index.html'))

    return render(request, 'post_update.html', {'form': form})
