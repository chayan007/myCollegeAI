from django import forms 
from profiles.models import Profile 


class ProfileForm(forms.ModelForm): 
    class Meta: 
        model = Profile 
        fields = '__all__'


class ChangePasswordForm(forms.Form):

    old_password = forms.CharField(max_length = 20,required=True)
    new_password = forms.CharField(max_length = 20,required=True)