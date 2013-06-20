from django import forms
from django.forms import ModelForm
from bross.pages.models import BrossContent
from django.utils.functional import lazy

class AddPageForm(ModelForm):
	class Meta:
		model = BrossContent

class EditPageForm(ModelForm):
	class Meta:
		model = BrossContent