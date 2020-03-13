from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError 
 
class EditProfileForm(UserChangeForm):

    class Meta:
        model = User()
        fields = (
            'first_name',
            'last_name',
            'email'
        )
