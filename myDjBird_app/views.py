#  views.py
#
#  by: Islam Diaa
#       17 Jul 2016
#
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from .models import Users, Timeline, Reply, Likes, Dislikes, FollowMe, IFollow
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

from django.core.context_processors import csrf


# Create your views here.
# @login_required
def index(request):
    return render_to_response('index.html', {
        'user': request.user,
        'timeline': Timeline.objects.all()[:10]
    })

def about(request):
    return render(request, 'about.html')

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
    user_details = Users.objects.get(user=request.user.id)
    return render(request, 'show_profile.html', {
        'user': request.user,
        'user_details': user_details,
    })
    # return render(request, 'show_profile.html', {
    #     'user': request.user,
    # })

@csrf_protect
def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # user = User.objects.create_user(
            #     username=form.cleaned_data['username'],
            #     password=form.cleaned_data['password1'],
            #     profile_picture=form.cleaned_data['profile_picture'],
            #     email=form.cleaned_data['email']
            # )
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

# def register_user(request):
#     if request.user.is_authenticated():
#         return HttpResponseRedirect('complete')
#         # return HttpResponseRedirect('/profile/')
#
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             user = User.objects.create_user(
#                 username=form.cleaned_data['username'],
#                 email=form.cleaned_data['email'],
#                 password=form.cleaned_data['password'])
#             user.save()
#
#             dj_user = Users(
#                 user=user,
#                 email=form.cleaned_data['email'],
#                 profile_picture=form.cleaned_data['profile_picture'],
#                 password=form.cleaned_data['password'])
#             dj_user.save()
#             return HttpResponseRedirect('complete')
#
#         else:
#             return render_to_response('registration/register.html', {"form": form},
#                                       context_instance=RequestContext(request))
#     else:
#         '''user is not submitting the form show a blank Registration Form'''
#         form = RegistrationForm()
#         context = {'form': form}
#         return render_to_response('registration/register.html', context, context_instance=RequestContext(request))

def register_success(request):
    return render_to_response('registration/success.html',)

def logout_page(request):
    logout(request)
    return render_to_response('registration/loggedout.html',)
    # return HttpResponseRedirect('registration/loggedout.html')

# @login_required
# def home(request):
#     return render_to_response('index.html', {'user': request.user})

# def register_user(request):
#     if request.method == 'POST':
#         form = Users(request.POST)
#         if form.is_valid():
#             new_user = Users(username=request.POST['username'],
#                              password=request.POST['password'],
#                              email=request.POST['email'],
#                              profile_picture=request.POST['profile_picture'])
#             new_user.save()
#             login(request, new_user)
#             return HttpResponseRedirect('/registration/success/')
#             # return HttpResponseRedirect(reverse('index.html'))
#     else:
#         form = Users()
#     token = {}
#     token.update(csrf(request))
#     token['form'] = form
#     return render(request, 'register.html', {'form': form})
#
# def register_success(request):
#     return render_to_response('registration/success.html',)
#
# def loggedin(request):
#     return render_to_response('registration/loggedin.html',
#                               {'username': request.user.username})
#
# def logout_page(request):
#     logout(request)
#     return HttpResponseRedirect('/')
#
# @login_required
# def home(request):
#     return render_to_response(
#         'index.html',
#         {'username': request.username }
#     )

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
        new_update = Timeline(user_id=request.POST['user_id'],
                              content=request.POST['content'])
        new_update.save()
        return HttpResponseRedirect(reverse('index.html'))

    return render(request, 'post_update.html', {'form': form})
