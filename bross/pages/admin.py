from django.contrib import admin
from bross.pages.models import BrossContent, BrossUser, BrossOption

class BrossContentAdmin(admin.ModelAdmin):
        prepopulated_fields = {'url': ('title',)}
        list_display = ('title', 'datetime')
        search_fields = ['title', 'datetime']

admin.site.register(BrossContent, BrossContentAdmin)
admin.site.register(BrossUser)
admin.site.register(BrossOption)