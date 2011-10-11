from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('trocpanier.views',
    url(r'^$','index',name="troc_index"),
    url(r'^depot/','depot',name='deposer'),
    url(r'^reserver/','reserver',name='reserver'),
    url(r'^lister/','lister',name='lister'),
)
