from django.contrib.auth.forms import UserCreationForm
from musicapp.jamusers.models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'password')