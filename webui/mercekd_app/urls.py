from django.conf.urls import patterns, include, url
from mercekd_app.views import anomalies, leases,display_subnets

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

    url(r'^anomalies/', view=anomalies, name='dns_anomalies'),
    url(r'^leases/$', view=leases, name='dns_leases'),
    url(r'^leases/(?P<subnet>(\d+).(\d+).(\d+))/$', view=display_subnets, name='display_subnet_view'),
)
