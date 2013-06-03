from django import forms
from django.forms import ModelForm
from bross.pages.models import Pages

class AddPageForm(forms.Form):
        title           = forms.CharField(label=(u'Title'))
        content         = forms.CharField(widget=forms.Textarea(attrs={'cols': 80, 'rows': 20}))