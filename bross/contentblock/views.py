from django.shortcuts import render
from django.http import HttpResponse
from bross.contentblock.models import *

def search_form(request):
    return render(request, 'search_form.html') 

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        return render(request, 'search_results.html',
            {'books': books, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')

def add(request):
	return render(request, 'add.html')

def show(request):
	return render(request, 'show.html')

def saveSubmit(request):
	if request.POST != '':
		p = Author(first_name=request.POST['firstname'], last_name=request.POST['lastname'], email='asdfasdf@daf.asd')
		p.save()
		return show(request)
	else:
		return HttpResponse('No values submited')

def content(request, id):
	cont = Content.objects.filter(id=id)
	return render(request, 'show.html', {'data': cont})