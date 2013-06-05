from django import forms
from django.forms import ModelForm
from bross.pages.models import Page
from django.utils.functional import lazy

TEMPLATE_CHOICES = (
		('L', 'Landing'),
		('B', 'Blog'),
		('G', 'Gallery'),
		('C', 'Contact'),
)

PARENT_CHOICES = (
		#dik automatisch gegenereerde lijst met parents
		('1', 'Parent 1'),
		('2', 'Parent 2'),
)

STATUS_CHOICES = (
		('P', 'Published'),
		('O', 'Offline'),
)


class AddPageForm(forms.Form):
        title           = forms.CharField(label=(u'Title'))
        content         = forms.CharField(widget=forms.Textarea(attrs={'cols': 80, 'rows': 20}))
        description		= forms.CharField()
        location		= forms.CharField()
        template    	= forms.ChoiceField(choices=TEMPLATE_CHOICES)
        parent			= forms.ChoiceField(choices=PARENT_CHOICES)
        status			= forms.ChoiceField(choices=STATUS_CHOICES)