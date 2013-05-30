from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template import RequestContext
from bross.account.forms import RegistrationForm
from bross.account.models import Account

def AccountRegistration(request):
        if request.user.is_authenticated():
                return HttpResponseRedirect('/profile/')
        if request.method == 'POST':
                form = RegistrationForm(request.POST)
                if form.is_valid():
                        user = User.objects.create_user(username=form.cleaned_data['username'], email =form.cleaned_data['email'], password = form.cleaned_data['password'])
                        user.save()
                        account = Account(user=user, name=form.cleaned_data['name']) 
                        account.save()
                        return HttpResponseRedirect('/profile/')
                else:
                        return render_to_response('register.html', {'form': form}, context_instance=RequestContext(request))
        else:
                ''' user is not submitting the form, show them a blank registration form '''
                form = RegistrationForm()
                context = {'form': form}
                return render_to_response('register.html', context, context_instance=RequestContext(request))