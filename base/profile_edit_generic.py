from django.views import View
from django.http import HttpResponse
from profiles.models import Profile 
from .forms import ProfileForm

class EditUserProfileView(View):
    form_class = ProfileForm

    def put(self, request, pk, format=None):
        profile =  Profile.objects.get(pk=pk)
        form = ProfileForm(profile, data=request.data)
        if form.is_valid():
            form.save()
            return HttpResponse(form.data)
        return HttpResponse(form.errors)