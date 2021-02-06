from django import forms 
from profiles.models import Profile 
from django.contrib.auth.password_validation import validate_password

class ProfileForm(forms.ModelForm): 
    class Meta: 
        model = Profile 
        fields = "__all__"


class ChangePasswordForm(forms.Form):

    old_password = forms.CharField(max_length = 200,required=True)
    new_password = forms.CharField(max_length = 200,required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value
