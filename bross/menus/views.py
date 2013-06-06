from django.shortcuts import render_to_response
from django.template import RequestContext
from bross.menus.models import Menu, Parent

def MenusAll(request):
        menus = Menu.objects.all().order_by('name')
        context = {'menus': menus}
        return render_to_response('menusall.html', context, context_instance=RequestContext(request))
