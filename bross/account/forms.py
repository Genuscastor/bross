from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from bross.account.models import Account

class RegistrationForm(ModelForm):
        name            = forms.CharField(label=(u'Name'))
        username        = forms.CharField(label=(u'User Name'))
        email           = forms.EmailField(label=(u'Email Address'))
        password        = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
        password1       = forms.CharField(label=(u'Verify Password'), widget=forms.PasswordInput(render_value=False))

        class Meta:
                model = Account
                exclude = ('user',)

        def clean_username(self):
                username = self.cleaned_data['username']
                try:
                        User.objects.get(username=username)
                except User.DoesNotExist:
                        return username
                raise forms.ValidationError("That username is already taken, please select another.")

        def clean(self):
                password = self.cleaned_data['password']
                if password != '':
                        if self.cleaned_data['password'] != self.cleaned_data['password1']:
                                raise forms.ValidationError("The passwords did not match.  Please try again.")
                        return self.cleaned_data
                else:
                        raise forms.ValidationError("Please fill in a password.")

class LoginForm(forms.Form):
        username        = forms.CharField(label=(u'User Name'), widget=forms.TextInput(attrs={'placeholder': 'Username'}))
        password        = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False, attrs={'placeholder': 'Password'}))
		
