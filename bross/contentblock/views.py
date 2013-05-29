from django.shortcuts import render
from django.http import HttpResponse
from bross.contentblock.models import Book
from django.core.mail import send_mail
from bross.contact.forms import ContactForm
from django.http import HttpResponseRedirect


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
