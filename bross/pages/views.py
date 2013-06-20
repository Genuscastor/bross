from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from bross.pages.forms import AddPageForm, EditPageForm
from bross.pages.models import BrossContent
from django.contrib.auth import authenticate, login, logout
import urllib

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
            return render_to_response('add_page.html', {'form': form}, context_instance=RequestContext(request))

    else:        
        form = AddPageForm()
        pages = BrossContent.objects.all().order_by('title')
        context = { 'form' : form, 'pages': pages }
        return render_to_response('add_page.html', context, context_instance=RequestContext(request))

def EditPage(request, url):
    page = BrossContent.objects.get(url=url)

    if request.method == 'POST':
        form = EditPageForm(request.POST, instance=page)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/pages/')
        else:
            print form.errors
            return HttpResponseRedirect('/dashboard/')

    else:
        form = EditPageForm(instance=page)
        pages = BrossContent.objects.all().order_by('title')
        context = {'form': form, 'pages': pages}
        return render_to_response('edit_page.html', context, context_instance=RequestContext(request))

def DeletePage(request, url):
    page = BrossContent.objects.get(url=url)
    page.delete()
    return HttpResponseRedirect('/pages/')


def ViewPage(request, url):
    page = BrossContent.objects.get(url=url)
    pages = BrossContent.objects.all().order_by('title')
    context = {'page': page, 'pages': pages}
    return render_to_response('sjaan_thema/base.html', context, context_instance=RequestContext(request))


def PagesAll(request):
    pages = BrossContent.objects.all().order_by('title')
    context = {'pages': pages}
    return render_to_response('pages.html', context, context_instance=RequestContext(request))










