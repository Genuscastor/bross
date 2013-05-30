from django.contrib import admin
from bross.contentblock.models import Publisher, Author, Book, Content


admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Content)
