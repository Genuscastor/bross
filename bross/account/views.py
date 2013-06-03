from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from bross.account.forms import RegistrationForm, LoginForm
from bross.account.models import Account
from django.contrib.auth import authenticate, login, logout

def AccountRegistration(request):
        if request.user.is_authenticated():
                return HttpResponseRedirect('/dashboard/')
        if request.method == 'POST':
                form = RegistrationForm(request.POST)
                if form.is_valid():
                        user = User.objects.create_user(username=form.cleaned_data['username'], email = form.cleaned_data['email'], password = form.cleaned_data['password'])
                        user.save()
                        account = Account(user=user, name=form.cleaned_data['name'])
                        account.save()
                        return HttpResponseRedirect('/dashboard/')
                else:
                        return render_to_response('register.html', {'form': form}, context_instance=RequestContext(request))
        else:
                ''' user is not submitting the form, show them a blank registration form '''
                form = RegistrationForm()
                context = {'form': form}
                return render_to_response('register.html', context, context_instance=RequestContext(request))

@login_required
def Dashboard(request):
        if not request.user.is_authenticated():
                return HttpResponseRedirect('/login/')
        account = request.user.get_profile
        context = {'account': account}
        return render_to_response('dashboard.html', context, context_instance=RequestContext(request))

def LoginRequest(request):
        if request.user.is_authenticated():
                return HttpResponseRedirect('/dashboard/')
        if request.method == 'POST':
                form = LoginForm(request.POST)
                if form.is_valid():
                        username = form.cleaned_data['username']
                        password = form.cleaned_data['password']
                        account = authenticate(username=username, password=password)
                        if account is not None:
                                login(request, account)
                                return HttpResponseRedirect('/dashboard/')
                        else:
                                return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))
                else:
                        return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))
        else:
                ''' user is not submitting the form, show the login form '''
                form = LoginForm()
                context = {'form': form}
                return render_to_response('login.html', context, context_instance=RequestContext(request))

def LogoutRequest(request):
        logout(request)
        return HttpResponseRedirect('/login/')