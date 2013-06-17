from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from core.controler.forms import AddPageForm
from core.models import BrossContent
from django.contrib.auth import authenticate, login, logout

@login_required
def Pages(request):
	return render_to_response('pages.html')

@login_required
def AddPage(request):
    if request.method == 'POST':
        form = AddPageForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/pages/')
        else:
            print form.errors
            return HttpResponseRedirect('/dashboard/')

    else:        
        form = AddPageForm()
        context = { 'form' : form }
        return render_to_response('add_page.html', context, context_instance=RequestContext(request))



