from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User



class SignupForm(UserCreationForm):
    username = forms.CharField(help_text='این نام کاربری در هنگام ورود به حساب خود لازم است', label='نام کاربری ')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


