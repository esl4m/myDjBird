#  views.py
#
#  by: Islam Diaa
#       17 Jul 2016
#
from .forms import RegistrationForm, PostUpdateForm
from django.contrib.auth.models import User
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Users, Timeline  # , Reply, Likes, Dislikes, FollowMe, IFollow
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

# from django.contrib.auth import authenticate, login
# from django.contrib.auth.forms import UserCreationForm
# from django.core.context_processors import csrf


# Create your views here.
def index(request):
    return render_to_response('index.html', {
        'user': request.user,
        'timeline': Timeline.objects.all()[:10]
    })


def about(request):
    return render(request, 'about.html')


@login_required(login_url='accounts/login/')
def post_update(request):
    # if request.method == 'POST':
    #     form = PostUpdateForm(request.POST)
    #     if form.is_valid():
    #         post = form.save(commit=False)
    #         post.user = request.user
    #         post.save()
    #         return redirect('index.html')
    # else:
    #     form = PostUpdateForm()
    # return render(request, 'post_update.html', {'form': form})

    # # form = Timeline(request.POST)
    form = PostUpdateForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        new_update = Timeline(
            user=request.user,
            content=form.cleaned_data['content'])
        new_update.save()
        return HttpResponseRedirect('/myDjBird_app/')
    return render(request, 'post_update.html', {'form': form})


def view_update(request):
    return render_to_response('view_update.html', {
        'update': get_object_or_404(Timeline)
    })


def list_users(request):
    return render(request, 'list_users.html', {
        'users': Users.objects.all(),
    })


@login_required(login_url='accounts/login/')
def show_profile(request):
    form = PostUpdateForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        new_update = Timeline(
            user=request.user,
            content=form.cleaned_data['content'])
        new_update.save()
        return HttpResponseRedirect('/myDjBird_app/show_profile')

    user_details = Users.objects.get(user=request.user)
    user_timeline = Timeline.objects.filter(user=request.user).order_by('-date')
    timeline_counts = Timeline.objects.filter(user=request.user).count()
    return render(request, 'show_profile.html', {
        'user': request.user,
        'user_details': user_details,
        'user_timeline': user_timeline,
        'timeline_counts': timeline_counts,
    })


@csrf_protect
def register_user(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/myDjBird_app/')

    elif request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password1'])
            user.save()

            dj_user = Users(
                user=user,
                email=form.cleaned_data['email'],
                profile_picture=request.FILES['profile_picture'],
                # profile_picture=form.cleaned_data['profile_picture'],
                password=form.cleaned_data['password1'])
            dj_user.save()
            return HttpResponseRedirect('complete')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {'form': form})
    return render_to_response('registration/register.html', variables,)


def register_success(request):
    return render_to_response('registration/success.html',)


def logout_page(request):
    logout(request)
    return render_to_response('registration/loggedout.html',)
    # return HttpResponseRedirect('registration/loggedout.html')

