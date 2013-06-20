from core.models import *
from django.shortcuts import render

def getBrossPage(request, page_url):
	#active = BrossContent.objects.get(url=page_url)
	#template = BrossOption.object.get(ActiveTemplate)
    return render(request, 'test.html', page_url)