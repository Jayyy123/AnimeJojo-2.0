from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from users.models import Profile


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name', 'username','email', 'password1','password2']


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'username', 'email', 'display_picture','bio','dob']
