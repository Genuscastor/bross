from django import forms
from django.forms import ModelForm
from bross.treemenus.models import MenuItem

class AddMenuForm(ModelForm):
	class Meta:
		model = MenuItem
