from django.contrib import admin
from bross.menus.models import Menu, Parent

class MenuAdmin(admin.ModelAdmin):
       # prepopulated_fields = {'slug': ('name',)}
        list_display = ('name', 'parent', 'description')
        search_fields = ['name']

class ParentAdmin(admin.ModelAdmin):
        #prepopulated_fields = {'slug': ('name',)}
        list_display = ('name', 'description')

admin.site.register(Menu, MenuAdmin)
admin.site.register(Parent, ParentAdmin)