from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.contrib import messages
from profiles.models import Profile 
from profiles.forms import ProfileForm,EditProfileForm
from profiles.forms import ChangePasswordForm


class Dashboard(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'v2/raw/dashboard.html', {})


class EditUserProfileView(View):

    def get(self, request, format=None):
        form = EditProfileForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        context = {
            'form':form,
            'profile_form': profile_form,
        }
        return render(request, 'v2/pages/protected/edit-profile.html', context) 

    def post(self, request, format=None):
        form = EditProfileForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile) 
       
        if form.is_valid() and profile_form.is_valid():
            user_form = form.save()
            custom_form = profile_form.save(False)
            custom_form.user = user_form
            custom_form.save()
            messages.success(request, 'Changed Successfully!!')
        context = {
            'form':form,
            'profile_form': profile_form,
        }
        return render(request, 'v2/pages/protected/edit-profile.html', context) 


class UpdatePassword(View):

    def get(self, request,  format=None):
        return render(request, 'v2/pages/protected/update-password.html', {}) 

    def post(self, request, format=None):
        user = request.user
        form = ChangePasswordForm(request.POST)

        if form.is_valid():
            old_password = form.data.get('old_password')
            if not user.check_password(old_password):
               messages.success(request, 'Wrong Password!!')
            else:
                user.set_password(form.data.get('new_password'))
                user.save()
                messages.success(request, 'Changed Successfully!!')
        context = {
            'form':form,
        }
        return render(request, 'v2/pages/protected/update-password.html', context)