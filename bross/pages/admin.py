from django.contrib import admin
from bross.pages.models import Page

class PagesAdmin(admin.ModelAdmin):
        prepopulated_fields = {'url': ('title',)}
        list_display = ('title', 'dateTime')
        search_fields = ['title', 'dateTime']

admin.site.register(Page, PagesAdmin)