from django.conf.urls import patterns, include, url
from django.contrib import admin
from core.views import *

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    (r'^tinymce/', include('tinymce.urls')),
    (r'^$', 'bross.editor.views.MainHomePage'),
    (r'^login/$', 'bross.account.views.LoginRequest'),
    (r'^logout/$', 'bross.account.views.LogoutRequest'),
    (r'^dashboard/$', 'bross.account.views.Dashboard'),
    (r'^resetpassword/passwordsent/$', 'django.contrib.auth.views.password_reset_done'),
    (r'^resetpassword/$', 'django.contrib.auth.views.password_reset'),
    (r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm'),
    (r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete'),
    (r'^pages/$', 'core.controlers.backend.views.Pages'),
    (r'^pages/add/$', 'core.controlers.backend.views.AddPage'),
    url(r'^(?P<page_url>.+?)/$', 'core.views.getBrossPage'),
)
