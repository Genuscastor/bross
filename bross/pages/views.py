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
# def AddPage(request):
# 	if request.method == 'POST':
#                 form = AddPageForm(request.POST)
#             	if form.is_valid():
#                         title = request.POST.get('title', '')
#                         content = request.POST.get('content', '')
#                         description = request.POST.get('description', '')
#                         location = request.POST.get('location', '')
#                         template = request.POST.get('template', '')
#                         parent = request.POST.get('parent', '')
#                         content_all = Page(title=title, content=content, description=descrition, location=location, template=template, parent=parent)
#                         content_all.save()
#                         #Opslaan die shit pages.save()
#                         return HttpResponseRedirect('/pages/')
#                 else:
#                         return render_to_response('add_page.html', {'form': form}, context_instance=RequestContext(request))
#                         print 'NENENENE'
#         else:
#                 ''' user is not submitting the form, show them a blank registration form '''
#                 form = AddPageForm()
#                 context = {'form': form}
#                 return render_to_response('add_page.html', context, context_instance=RequestContext(request))
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



