from django import forms
from django.forms import ModelForm
from bross.pages.models import Page

class AddPageForm(forms.Form):
        title           = forms.CharField(label=(u'Title'))
        url				= forms.SlugField()
        content         = forms.CharField(widget=forms.Textarea(attrs={'cols': 80, 'rows': 20}))
        description		= forms.CharField()
        location		= forms.CharField()
        template    	= forms.CharField()
        parent			= forms.CharField()
        menu			= forms.CharField()
        status			= forms.CharField()