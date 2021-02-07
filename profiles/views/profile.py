from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from profiles.models import Profile 
from profiles.forms import ProfileForm
from profiles.forms import ChangePasswordForm


class Dashboard(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'pages/protected/dashboard.html', {})


class EditUserProfileView(View):
    form_class = ProfileForm

    def get(self, request, pk, format=None):
        return render(request, 'pages/auth/edit-profile.html', {}) 

    def post(self, request, pk, format=None):
        profile = request.user.profile
        form = ProfileForm(profile, data=request.data)
        message = ''
        if form.is_valid():
            form.save()
            message = 'Changed Successfully!!'
        context = {
            'message':message,
        }
        return render(request, 'pages/auth/edit-profile.html', context) 


class UpdatePassword(View):
    form_class = ChangePasswordForm

    def get(self, request, pk, format=None):
        return render(request, 'pages/auth/change-password.html', {}) 


    def post(self, request, pk, format=None):
        user = self.request.user
        form = ChangePasswordForm(data=request.data)
        message = ''
        if form.is_valid():
            old_password = form.data.get('old_password')
            if not user.check_password(old_password):
               message = 'Wrong Password!!'
            else:
                user.set_password(form.data.get('new_password'))
                user.save()
                message = 'Changed Successfully!!'
        context = {
            'message':message,
        }
        return render(request, 'pages/auth/change-password.html', context) 
