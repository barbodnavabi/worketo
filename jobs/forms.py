from .models import massage
from django.forms import ModelForm
from django import forms

class MassegeForm(forms.ModelForm):
    
    class Meta:
        model = massage
        fields = ['name','pdf',"phone","email"]