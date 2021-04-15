from .models import massage
from django.forms import ModelForm
from django import forms
from tinymce.widgets import TinyMCE
from .models import Jobs
class MassegeForm(forms.ModelForm):
    
    class Meta:
        model = massage
        fields = ['name','pdf',"phone","email"]





class JobForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(JobForm, self).__init__(*args, **kwargs)
        self.fields['description']= forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Jobs
        fields = [
        "title",
        "company",
        "description",
        "address",
        "important",
        "price",
        "category",
        "state",
        "Type",
        "soldiering",
        "sex",
        'service',
        'employer_description', ]
