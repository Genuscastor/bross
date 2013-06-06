from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from bross.pages.forms import AddPageForm
from bross.pages.models import Page
from django.contrib.auth import authenticate, login, logout

@login_required
def Pages(request):
	return render_to_response('pages.html')

@login_required
def AddPage(request):
	if request.method == 'POST':
                form = AddPageForm(request.POST)
            	if form.is_valid():
                        p = Page(title='test', content='test', description='test', location='test', template='test', parent='test', menu='test', status='test')
                        p.save()
                        #Opslaan die shit pages.save()
                        return HttpResponseRedirect('/pages/')
                else:
                        return render_to_response('add_page.html', {'form': form}, context_instance=RequestContext(request))
        else:
                ''' user is not submitting the form, show them a blank registration form '''
                form = AddPageForm()
                context = {'form': form}
                return render_to_response('add_page.html', context, context_instance=RequestContext(request))



