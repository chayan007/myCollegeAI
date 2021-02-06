from django.views import View
from django.http import HttpResponse
from .forms import ChangePasswordForm

class UpdatePassword(View):
    form_class = ChangePasswordForm

    def put(self, request, *args, **kwargs):
        self.object = self.request.user
        form = ChangePasswordForm(data=request.data)

        if form.is_valid():
            old_password = form.data.get("old_password")
            if not self.object.check_password(old_password):
                return HttpResponse({"old_password": ["Wrong password."]} )
            self.object.set_password(form.data.get("new_password"))
            self.object.save()
            return HttpResponse("Successfully Changed!!")

        return HttpResponse(form.errors)