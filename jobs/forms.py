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
        self.fields['description']= forms.CharField(widget=TinyMCE(attrs={'cols': 10, 'rows': 5}))
        self.fields['employer_description']= forms.CharField(widget=TinyMCE(attrs={'cols': 10, 'rows': 5}))
        self.fields['description'].label='توضیحات'
        self.fields['employer_description'].label='شرح شغلی' 
        self.fields["important"].widget.attrs['class'] = 'form-control'
        self.fields["important"].widget.attrs['data-role'] = 'tagsinput'
        self.fields["important"].help_text=None
        self.fields["service"].widget.attrs['class'] = 'form-control'
        self.fields["service"].widget.attrs['data-role'] = 'tagsinput'
        self.fields["service"].help_text=None

    class Meta:
        model = Jobs
        fields = [
        "title","company","description","address","important","price",
        "category","state","Type","soldiering","sex",'service','employer_description','experiance' ]
