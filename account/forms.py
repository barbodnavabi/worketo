from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')

        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        # self.fields['special_user'] = SplitJalaliDateTimeField(label='کاربر ویژه تا',
        #                                                        widget=AdminSplitJalaliDateTime
        #                                                        )

        if not user.is_superuser:
            self.fields['username'].disabled = True
            self.fields['special_user'].disabled = True

    class Meta:
        model = User
        fields = ['username','email', 'first_name', 'last_name', 'special_user', "phone", "avatar"]

class SignupForm(UserCreationForm):
    username = forms.CharField(help_text='این نام کاربری در هنگام ورود به حساب خود لازم است', label='نام کاربری ')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


