from django.conf.urls.defaults import patterns, include, url
from bross.views import hello, current_datetime, hours_ahead
from bross.contentblock import views
#Deze import werkt niet en daardoor gaat alles stuk.
# from bross.contact import views 
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search),
    url(r'^add/$', views.add),
    url(r'^show/(\d)/$', views.content),
    url(r'^save/$', views.saveSubmit),

    #deze aanzetten als import werkt
    # url(r'^contact/$', views.contact),

    # Examples:
    # url(r'^$', 'bross.views.home', name='home'),
    # url(r'^bross/', include('bross.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
