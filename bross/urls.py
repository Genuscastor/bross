from django.conf.urls import patterns, include, url
from bross.views import hello, current_datetime, hours_ahead
from bross.contentblock.views import search_form, search, add, show, saveSubmit, content
#Deze import werkt niet en daardoor gaat alles stuk.
from bross.contact.views import contact
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^search-form/$', search_form),
    url(r'^search/$', search),
    url(r'^add/$', add),
    url(r'^show/(\d)/$', content),
    url(r'^save/$', saveSubmit),
    (r'^register/$', 'bross.account.views.AccountRegistration'),
    (r'^beers/$', 'bross.beer.views.BeersAll'),
    (r'^beers/(?P<beerslug>.*)/$', 'bross.beer.views.SpecificBeer'),
    (r'^brewerys/(?P<breweryslug>.*)/$', 'bross.beer.views.SpecificBrewery'),
    (r'^login/$', 'bross.account.views.LoginRequest'),
    (r'^logout/$', 'bross.account.views.LogoutRequest'),


    #deze aanzetten als import werkt
    url(r'^contact/$', contact),

    # Examples:
    # url(r'^$', 'bross.views.home', name='home'),
    # url(r'^bross/', include('bross.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
