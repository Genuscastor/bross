from django.conf.urls import patterns, include, url
from django.contrib import admin
from core.views import *

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^(?P<page_url>.+?)/$', 'core.views.getBrossPage'),
    url(r'^admin/', include(admin.site.urls)),
)
