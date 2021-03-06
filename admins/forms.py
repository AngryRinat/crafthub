
from django import forms

from users.forms import UserRegistrationForm, UserProfileForm
from users.models import User


class UserAdminRegisterForm(UserRegistrationForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'image', 'first_name', 'last_name', 'password1', 'password2')


class UserAdminProfileForm(UserProfileForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'readonly': False}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'readonly': False}))