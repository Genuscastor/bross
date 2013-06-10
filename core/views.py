from core.models import *
from django.shortcuts import render

def getBrossPage(request, page_url):
	#active = BrossContent.objects.get(url=page_url)
    return render(request, 'test.html', page_url)