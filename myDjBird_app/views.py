#  views.py
#
#  by: Islam Diaa
#       17 Jul 2016
#
from .forms import RegistrationForm, PostUpdateForm, PostReplyForm
from django.contrib.auth.models import User
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Users, Timeline, Replies, Likes, Dislikes, Follow
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from collections import Counter
from django.core.exceptions import PermissionDenied

# Create your views here.
def index(request):
    if request.user.is_authenticated():
        user = request.user
        # Check if user follows others users .. display their timeline.
        i_follow = Follow.objects.filter(follower=user)  # get all users I follow !
        i_follow = i_follow.values_list('following')
        i_follow = [int(e[0]) for e in i_follow]  # Get all user ids in a list
        i_follow.append(user.id)  # Append list with current user (the timeline contains followers and the current user)
        # Then get all timeline (me and users i follow) show the latest 50 tweets
        timeline = Timeline.objects.filter(user_id__in=i_follow).order_by('-date')[:49]
    else:
        user = ''
        timeline = ''
    # Get the most active user and display his latest status !
    most_active_user = Counter(Timeline.objects.order_by('-date').values_list('user_id', flat=True).distinct())
    most_active_user = most_active_user.most_common(1)[0][0]
    recommended = Timeline.objects.filter(user_id=most_active_user).order_by('-date')[0]  # get latest status for the most active user.
    return render_to_response('index.html', {
        'user': user,
        'timeline': timeline,
        'recommended': recommended,
    })


def about(request):
    return render(request, 'about.html')


@login_required(login_url='/myDjBird_app/accounts/login/')
def post_update(request):
    form = PostUpdateForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        new_update = Timeline(
            user=request.user,
            content=form.cleaned_data['content'])
        new_update.save()
        return HttpResponseRedirect('/myDjBird_app/')
    return render(request, 'post_update.html', {'form': form})


def list_users(request):
    if request.user.is_authenticated():
        i_follow = Follow.objects.filter(follower=request.user)  # get all users I follow !
        i_follow = i_follow.values_list('following')
        i_follow = [int(e[0]) for e in i_follow]  # Get all user ids in a list
    else:
        i_follow = ''
    return render(request, 'list_users.html', {
        'users': Users.objects.all(),
        'i_follow': i_follow,
    })


@login_required(login_url='/myDjBird_app/accounts/login/')
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
    if request.user.is_authenticated():
        i_follow = Follow.objects.filter(follower=request.user).count()  # (I follow means : follower == me !)
        follow_me = Follow.objects.filter(following=request.user).count()  # follow me means : following == me!)
    else:
        i_follow = ''
        follow_me = ''
    return render(request, 'show_my_profile.html', {
        'user': request.user,
        'user_details': user_details,
        'user_timeline': user_timeline,
        'timeline_counts': timeline_counts,
        'i_follow': i_follow,
        'follow_me': follow_me,
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
    i_follow = Follow.objects.filter(follower=user).count()  # (I follow means : follower == me !)
    follow_me = Follow.objects.filter(following=user).count()  # follow me means : following == me!)
    return render(request, 'view_profile.html', {
        'users': get_object_or_404(User, pk=user_id),
        'user_details': user_details,
        'user_timeline': user_timeline,
        'timeline_counts': timeline_counts,
        'i_follow': i_follow,
        'follow_me': follow_me,
    })


def search_users(request, user_name):
    user_name = str(user_name)
    try:  # if user exists
        user_id = User.objects.get(username=user_name).pk
        return HttpResponseRedirect('/myDjBird_app/view_user_profile/%s' % user_id)

    except User.DoesNotExist:
        print("user doesn't exists")
        return HttpResponseRedirect('/myDjBird_app/list_users')


def search_tweets(request, status_id):
    try:  # if tweet exists in timeline
        status_id = int(status_id)
        tweet = Timeline.objects.get(pk=status_id)
        return HttpResponseRedirect('/myDjBird_app/view_post/%s' % tweet.id)
    except Timeline.DoesNotExist:
        print("Tweet doesn't exists")
        return HttpResponseRedirect('/myDjBird_app/show_profile')
    except ValueError:
        print("Value error not int")
        return HttpResponseRedirect('/myDjBird_app/show_profile')

def view_post(request, status_id):
    status_id = int(status_id)
    likes_count = Likes.objects.filter(status_id=status_id).count()
    dislikes_count = Dislikes.objects.filter(status_id=status_id).count()
    post = get_object_or_404(Timeline, pk=status_id)
    user_details = Users.objects.get(user=post.user)
    replies = Replies.objects.filter(status_id=status_id).order_by('-date')
    reply_count = replies.count()
    # user_reply_details = Users.objects.get(user=replies.user)
    return render(request, 'view_status.html', {
        'post': post,
        'likes_count': likes_count,
        'dislikes_count': dislikes_count,
        'user_details': user_details,
        'replies': replies,
        'reply_count': reply_count,
        # 'user_reply_details': user_reply_details,
    })


@login_required(login_url='/myDjBird_app/accounts/login/')
def post_reply(request, status_id):
    status_id = int(status_id)
    timeline_id = Timeline.objects.get(id=status_id)
    reply_form = PostReplyForm(data=request.POST)
    if request.method == 'POST' and reply_form.is_valid():
        new_update = Replies(
            user=request.user,
            status_id=timeline_id,
            content=reply_form.cleaned_data['content'])
        new_update.save()
        return HttpResponseRedirect('/myDjBird_app/view_post/%s' % status_id)
    else:
        reply_form = PostReplyForm()
    return render(request, 'post_reply.html', {'reply_form': reply_form})


@login_required(login_url='/myDjBird_app/accounts/login/')
def post_delete(request, status_id):
    status_id = int(status_id)
    del_post = Timeline.objects.get(id=status_id)
    if del_post.user == request.user:  # check if this tweet by the user or not , if not he can't delete it.
        del_post.delete()
    else:
        print("You can't delete this post")  # TO_DO : return this error to user ..
    return HttpResponseRedirect('/myDjBird_app/show_profile')  # Redirect him to his profile after deleting !


@login_required(login_url='/myDjBird_app/accounts/login/')
def follow(request, user_id):
    """
    Method is used to follow user.
    """
    response = {}
    # Verify ajax request
    if request:
        user = request.user
        usr_key = User.objects.get(id=int(user_id))  # Getting the username #
        # Query user to follow
        try:
            usr2folw = User.objects.get(username=usr_key)
        except:
            response['success'] = False
            response['message'] = 'Unable to Follow now.'
        # Follow process. create master and slave.
        # slave follows master. Update followers count
        # and following count once done.
        try:
            obj, created = Follow.objects.get_or_create(follower=user, following=usr2folw)
            if created:
                master = Follow.objects.get(user=usr2folw)
                slave = Follow.objects.get(user=user)
                master.follower_count = master.follower_count+1
                slave.following_count = slave.following_count+1
                master.save()
                slave.save()

                response['success'] = True
                response['message'] = 'Following %s now.' % (usr2folw.username)
        except:
            response['success'] = False
            response['message'] = 'Unable to Follow %s now.' % (usr2folw.username)
    else:
        response['success'] = False
        response['message'] = 'Your request can not be served now.'

    return HttpResponseRedirect('/myDjBird_app/list_users/', response)


@login_required(login_url='/myDjBird_app/accounts/login/')
def unfollow(request, user_id):
    """
    Method is used to unfollow an user.
    """
    response = {}
    # Verify ajax request
    if request:
        user = request.user
        usr_key = User.objects.get(id=int(user_id))  # Getting the username #

        # Query user to unfollow
        try:
            usr2unfolw = User.objects.get(username=usr_key)
        except:
            response['success'] = False
            response['message'] = 'Unable to UnFollow now.'

        # Same logic as above but in reverse manner.
        try:
            obj = Follow.objects.get(follower=user, following=usr2unfolw).delete()

            master = Follow.objects.get(user=usr2unfolw)
            slave = Follow.objects.get(user=user)
            master.follower_count = master.follower_count-1
            slave.following_count = slave.following_count-1
            master.save()
            slave.save()

            response['success'] = True
            response['message'] = '''Successfully unfollowed to %s now.''' % usr2unfolw.username

        except:
            response['success'] = False
            response['message'] = 'Unable to unfollow %s now.' %(usr2unfolw.username)

    else:
        response['success'] = False
        response['message'] = 'Your request can not be served now.'

    return HttpResponseRedirect('/myDjBird_app/list_users/', response)


@login_required(login_url='/myDjBird_app/accounts/login/')
def post_like(request, status_id):
    status_id = int(status_id)
    timeline_id = Timeline.objects.get(id=status_id)
    # print(timeline_id.user, '///////', request.user)
    # print(status_id, '/////////', request.user)
    likes = Likes.objects.filter(status_id=status_id)
    users_like = likes.values_list('user', flat=True)
    if request.user.id in users_like:
        # User already liked it before #
        print('Already Liked !')
        # raise PermissionDenied
    else:
        new_like = Likes(
            user=request.user,
            status_id=timeline_id,
        )
        new_like.save()
    return HttpResponseRedirect('/myDjBird_app/view_post/%s' % status_id)


@login_required(login_url='/myDjBird_app/accounts/login/')
def post_dislike(request, status_id):
    status_id = int(status_id)
    timeline_id = Timeline.objects.get(id=status_id)

    dislikes = Dislikes.objects.filter(status_id=status_id)
    users_dislike = dislikes.values_list('user', flat=True)

    if request.user.id in users_dislike:
        # User already liked it before #
        print('Already Disliked !')
        # raise PermissionDenied
    else:
        new_dislike = Dislikes(
            user=request.user,
            status_id=timeline_id,
        )
        new_dislike.save()
    return HttpResponseRedirect('/myDjBird_app/view_post/%s' % status_id)


def logout_page(request):
    logout(request)
    return render_to_response('registration/loggedout.html',)
    # return HttpResponseRedirect('registration/loggedout.html')