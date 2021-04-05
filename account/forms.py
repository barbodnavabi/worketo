from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User



class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, required=False, help_text='ایمیل کاملا اختیاری است و نیاز به پر کردن نیست',
                             label='ایمیل (اختیاری)')
    username = forms.CharField(help_text='این نام کاربری در هنگام ورود به حساب خود لازم است', label='نام کاربری ')
    first_name = forms.CharField(help_text=' فیلد نام شما اجباری نیست', label='نام ', required=False)
    last_name = forms.CharField(help_text=' فیلد نام خوانوادگی شما اجباری نیست', label='نام خانوادگی', required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2','phone')


