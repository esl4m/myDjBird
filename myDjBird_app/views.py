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
from .models import Users, Timeline, Reply, Likes, Dislikes, FollowMe, IFollow
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    print(request.GET.getlist('myvar'))
    timeline = Timeline.objects.all().order_by('-date')[:49]
    likes_count = Likes.objects.filter(status_id=1).count()
    dislikes_count = Dislikes.objects.filter(status_id=1).count()
    return render_to_response('index.html', {
        'user': request.user,
        'timeline': timeline,
        'likes_count': likes_count,
        'dislikes_count': dislikes_count,
        # 'timeline': Timeline.objects.all()[:10]
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


def list_users(request):
    return render(request, 'list_users.html', {
        'users': Users.objects.all(),
    })


@login_required(login_url='accounts/login/')
def show_my_profile(request):
    form = PostUpdateForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        new_update = Timeline(
            user=request.user,
            content=form.cleaned_data['content'])
        new_update.save()
        return HttpResponseRedirect('/myDjBird_app/show_profile')

    user_details = Users.objects.get(user=request.user)
    user_timeline = Timeline.objects.filter(user=request.user).order_by('-date')[:49]
    timeline_counts = Timeline.objects.filter(user=request.user).count()
    return render(request, 'show_my_profile.html', {
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

            if not request.FILES:
                profile_pic = "default-pic.jpg"
            else:
                profile_pic = request.FILES['profile_picture']
            dj_user = Users(
                user=user,
                email=form.cleaned_data['email'],
                profile_picture=profile_pic,
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


def view_user_profile(request, user_id):
    user_id = int(user_id)
    user = User.objects.get(id=user_id)  # Getting the username #

    user_details = Users.objects.get(user=user)
    user_timeline = Timeline.objects.filter(user=user).order_by('-date')[:49]
    timeline_counts = Timeline.objects.filter(user=user).count()

    return render(request, 'view_profile.html', {
        'users': get_object_or_404(User, pk=user_id),
        'user_details': user_details,
        'user_timeline': user_timeline,
        'timeline_counts': timeline_counts,
    })


def view_post(request, status_id):
    status_id = int(status_id)
    likes_count = Likes.objects.filter(status_id=status_id).count()
    dislikes_count = Dislikes.objects.filter(status_id=status_id).count()
    return render(request, 'view_status.html', {
        'post': get_object_or_404(Timeline, pk=status_id),
        'likes_count': likes_count,
        'dislikes_count': dislikes_count,
    })


@login_required
def post_like(request, status_id):
    status_id = int(status_id)
    timeline_id = Timeline.objects.get(id=status_id)
    new_like = Likes(
        user=request.user,
        status_id=timeline_id,
    )
    new_like.save()
    return HttpResponseRedirect('/myDjBird_app/')


@login_required
def post_dislike(request, status_id):
    status_id = int(status_id)
    timeline_id = Timeline.objects.get(id=status_id)
    new_dislike = Dislikes(
        user=request.user,
        status_id=timeline_id,
    )
    new_dislike.save()
    return HttpResponseRedirect('/myDjBird_app/')


def logout_page(request):
    logout(request)
    return render_to_response('registration/loggedout.html',)
    # return HttpResponseRedirect('registration/loggedout.html')