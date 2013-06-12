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

MENU_CHOICES = (
		#dik automatisch gegenereerde lijst met menus
		('1', 'Menu 1'),
		('2', 'Menu 2'),
)

STATUS_CHOICES = (
		('P', 'Published'),
		('O', 'Offline'),
)


class AddPageForm(ModelForm):
	class Meta:
		model = Page