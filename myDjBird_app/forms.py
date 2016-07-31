#  models.py
#
#  by: Islam Diaa
#       17 Jul 2016
#

from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.core.files.images import get_image_dimensions
from .models import Replies  # Timeline

class RegistrationForm(forms.Form):
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(
        attrs=dict(required=True, max_length=30)),
        label=_("Username"),
        error_messages={'invalid': _("This value must contain only letters, numbers and underscores.")})
    email = forms.EmailField(widget=forms.EmailInput(
        attrs=dict(required=True, max_length=30)),
        label=_("Email address"))
    if forms.FileField(required=False):
        profile_picture = forms.FileField(required=False)
    else:
        profile_picture = None
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs=dict(required=True, max_length=30, render_value=False)),
        label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs=dict(required=True, max_length=30, render_value=False)),
        label=_("Password (again)"))

    def clean_username(self):
        # username = self.cleaned_data['username']
        # try:
        #     User.objects.get(username=username)
        # except User.DoesNotExist:
        #     return username
        # raise forms.ValidationError('The username is already taken. Please try with another')

        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The username already exists. Please try another one."))

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data

    def clean_avatar(self):
        avatar = self.cleaned_data['profile_picture']
        try:
            w, h = get_image_dimensions(avatar)

            # validate dimensions
            max_width = max_height = 100
            if w > max_width or h > max_height:
                raise forms.ValidationError(
                    u'Please use an image that is %s x %s pixels or smaller.' % (max_width, max_height))

            # validate content type
            main, sub = avatar.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
                raise forms.ValidationError(u'Please use a JPEG, ''GIF or PNG image.')

            # validate file size
            if len(avatar) > (20 * 1024):
                raise forms.ValidationError( u'Avatar file size may not exceed 20k.')

        except AttributeError:
            """
            Handles case when we are updating the user profile
            and do not supply a new avatar
            """
            pass

        return avatar

class PostUpdateForm(forms.Form):
    # content = forms.Textarea()
    content = forms.CharField(required=True, max_length=250, widget=forms.Textarea)
    # class Meta:
    #     model = Timeline
    #     fields = ('content',)

class PostReplyForm(forms.Form):
    content = forms.CharField(required=True, max_length=250, widget=forms.Textarea)

    class Meta:
        model = Replies

