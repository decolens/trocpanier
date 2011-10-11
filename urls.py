from django.conf.urls.defaults import patterns, include, url

from django.views.generic import RedirectView
from django.core.urlresolvers import reverse

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',

## redirection
#    url(r'^$', RedirectView.as_view(url=reverse("troc_index"))),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

## module auth std
    url(r'^accounts/',include('django.contrib.auth.urls')),
    url(r'^',include('trocpanier.urls')),
)
