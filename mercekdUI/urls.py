from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.views.generic import ListView, DetailView
from mercekdUI.main.models import Lease



# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
leases_list = ListView.as_view(model=Lease)
urlpatterns = patterns('',
   # url(r'^$', leases_list, name='leases_list'),
    
    url(r'^$', 'mercekdUI.main.views.home', name='homePage'),
    url(r'^listLeases/(?P<leases>\w+)$', 'mercekdUI.main.views.listLeases', name='listLeases'),
    # Examples:
    # url(r'^$', 'mercekdUI.views.home', name='home'),
    # url(r'^mercekdUI/', include('mercekdUI.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )
