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
    (r'^tinymce/', include('tinymce.urls')),
    (r'^$', 'bross.editor.views.MainHomePage'),
    (r'^register/$', 'bross.account.views.AccountRegistration'),
    (r'^beers/$', 'bross.beer.views.BeersAll'),
    (r'^beers/(?P<beerslug>.*)/$', 'bross.beer.views.SpecificBeer'),
    (r'^brewerys/(?P<breweryslug>.*)/$', 'bross.beer.views.SpecificBrewery'),
    (r'^login/$', 'bross.account.views.LoginRequest'),
    (r'^logout/$', 'bross.account.views.LogoutRequest'),
    (r'^dashboard/$', 'bross.account.views.Dashboard'),
    (r'^pages/$', 'bross.pages.views.PagesAll'),
    (r'^pages/add/$', 'bross.pages.views.AddPage'),
    (r'^pages/edit/(?P<url>.*)/$', 'bross.pages.views.EditPage'),
    (r'^pages/delete/(?P<url>.*)/$', 'bross.pages.views.DeletePage'),
    (r'^$', 'bross.account.views.LoginRequest'),    
    # (r'^themes/$', 'bross.themes.views.Themes'),
    # (r'^menus/$', 'bross.menus.views.Menus'),
    # (r'^modules/$', 'bross.modules.views.Modules'),
    (r'^resetpassword/passwordsent/$', 'django.contrib.auth.views.password_reset_done'),
    (r'^resetpassword/$', 'django.contrib.auth.views.password_reset'),
    (r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm'),
    (r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete'),
        

    #deze aanzetten als import werkt
    url(r'^contact/$', contact),

    # Examples:
    # url(r'^$', 'bross.views.home', name='home'),
    # url(r'^bross/', include('bross.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),


    (r'^(?P<url>.*)/$', 'bross.pages.views.ViewPage'),

)
