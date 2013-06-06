from django.shortcuts import render_to_response
from django.template import RequestContext
from bross.menus.models import Menu, Parent

def MenusAll(request):
        parent = Parent.objects.all().order_by('name')
        menus = Menu.objects.all().order_by('name')
        context = {'menus': menus, 'parent': parent}
        return render_to_response('menusall.html', context, context_instance=RequestContext(request))