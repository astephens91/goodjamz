from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from musicapp.jamusers.models import CustomUser
from django.contrib.auth import get_user_model
User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

class SignupForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email',)

